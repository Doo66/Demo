import sqlite3
from flask import (Flask, render_template, g, flash, request, session, abort,
        redirect, url_for)


# 配置项
DATABASE = '/tmp/flaskr.db'
ENV = 'development'
DEBUG = True
SECRET_KEY = 'ADSFASDF'
USERNAME = 'James'
PASSWORD = 'SYL'


app = Flask(__name__)
# app.config 的 from_object 方法通常用于获取对象的属性以增加配置项
# 此处使用的参数为 __name__ ，也就是当前所在文件
# 结果就是读取当前所在文件中的所有变量，选择其中全大写的变量作为配置项
app.config.from_object(__name__)


# 此函数的返回值是 sqlite3.connect 方法的调用，也就是连接对象
# 这里之所以写一个函数，是因为后面的代码会多次用到连接对象
def db_conn():
    '''创建与数据库连接的对象
    '''

    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    '''此函数用于创建数据表，需要在 flask shell 里引入执行
    '''

    # db_conn 函数的返回值是 sqlite3.connect 方法的返回值
    # sqlite3.connect 方法的返回值是具有 __enter__ 和 __exit__ 两个特殊方法的上下文对象
    # 这个上下文对象也叫连接对象，它的存在就是和 sqlite3 数据库保持连接的标志
    # 其中 as 关键字后面的 conn 就是连接对象，该对象有一个 close 方法用于关闭连接
    # 此处使用 with 关键字处理 sqlite3.connect 方法的返回值
    # 使得 with 语句块内的代码运行完毕后自动执行连接对象 conn 的 close 方法关闭连接
    with db_conn() as conn:
        # app.open_resource 方法的返回值也是上下文对象
        # 这个上下文对象也叫 IO 包装对象，是文件读取到内存后的数据包
        # 此对象同样有一个 close 方法需要必须执行以关闭文件
        # 变量 f 就是 IO 包装对象，它的 read 方法的返回值是文件内容的二进制格式
        with app.open_resource('schema.sql') as f:
            # 连接对象 conn 的 cursor 方法的返回值是一个光标对象，用于执行 SQL 语句
            # 该光标对象通常使用 execute 执行 SQL 语句，参数为语句的字符串
            # 光标对象的 executescript 可以一次执行多个 SQL 语句
            # 参数为多个语句的二进制格式，多个语句通常写到一个文件里
            conn.cursor().executescript(f.read().decode())
        # 连接对象的 commit 方法用于提交之前执行 SQL 语句的结果到数据库
        # 因为有些语句执行后不会立即改动数据库
        conn.commit()


# 这个装饰器的功能是，当任意视图函数执行时，预先执行这个装饰器下的所有函数
@app.before_request
def before():
    '''创建数据库的连接对象，并将其赋值给 g 的 conn 属性
    '''

    # Flask 应用中有两种上下文对象：应用上下文对象和请求上下文对象
    # g 是一个应用上下文对象，它的生存周期却是一次请求的收发
    # 也就是说，应用每收到一次请求就会生成一个 g 对象
    # 在生存周期内，它可以在任意视图函数中被使用
    g.conn = db_conn()


# 与 app.before_request 相对的是 app.after_request
# 后者在任意视图函数执行完毕之后执行，除非视图函数执行时遇到异常
# 而 app.teardown_request 装饰器与 app.after_request 作用一样
# 但它无视视图函数触发的任何异常，保证一定被执行
# 其中的参数为可能出现的异常
@app.teardown_request
def teardown(exception):
    '''关闭与数据库的连接
    '''

    g.conn.close()


@app.route('/')
def show_entries():
    '''显示所有存储在数据表中的条目
    '''

    # 获取连接对象执行查询操作之后的光标对象，该对象的 fetchall 方法中存储了查询结果
    cursor = g.conn.execute('SELECT title, text FROM entries ORDER BY id DESC')
    # 查询结果是一个列表，列表里是元组，将元组转换成字典
    entries = [dict(title=row[0], text=row[1]) for row in cursor.fetchall()]
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    '''添加一条博客
    '''

    if not session.get('login'):
        abort(401)
    g.conn.execute('INSERT INTO entries (title, text) VALUES (?, ?)',
            [request.form.get('title'), request.form.get('text')])
    g.conn.commit()
    flash('New entry has beensuccessfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''用户登录
    '''

    error = None
    if request.method == 'POST':
        if request.form.get('username') != app.config.get('USERNAME'):
            error = 'Invalid username'
        elif request.form.get('password') != app.config.get('PASSWORD'):
            error = 'Invalid password'
        else:
            session['login'] = True
            flash('You\'re loginned successfully!')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    '''用户登出
    '''

    session.pop('login', None)
    flash('You have logouted successfully')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    app.run()
