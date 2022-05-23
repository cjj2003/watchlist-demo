import os, sys
from flask import Flask, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
# from flask_restx import Resource, Api

app = Flask(__name__)
WIN	=	sys.platform.startswith('win')
if	WIN:		#	如果是	Windows	系统，使用三个斜线
	prefix	=	'sqlite:///'
else:		#	否则使用四个斜线
	prefix	=	'sqlite:////'

app.config['SQLALCHEMY_DATABASE_URI']	=	prefix	+	os.path.join(app.root_path + '/db/data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']	=	False		#	关闭对模型修改的监控


#	在扩展类实例化前加载配置
db = SQLAlchemy(app)

# api = Api(app)

name_00	=	'Grey	Li'
movies_00	=	[
				{'title':	'My00	Neighbor	Totoro',	'year':	'1988'},
				{'title':	'Dead	Poets	Society',	'year':	'1989'},
				{'title':	'A	Perfect	World',	'year':	'1993'},
				{'title':	'Leon',	'year':	'1994'},
				{'title':	'Mahjong',	'year':	'1996'},
				{'title':	'Swallowtail	Butterfly',	'year':	'1996'},
				{'title':	'King	of	Comedy',	'year':	'1999'},
				{'title':	'Devils	on	the	Doorstep',	'year':	'1999'},
				{'title':	'WALL-E',	'year':	'2008'},
				{'title':	'The	Pork	of	Music',	'year':	'2012'},
]

class	User(db.Model):		#	表名将会是	user（自动生成，小写处理）
	id	=	db.Column(db.Integer,	primary_key=True)		#	主键
	name	=	db.Column(db.String(20))		#	名字
class	Movie(db.Model):		#	表名将会是	movie
	id	=	db.Column(db.Integer,	primary_key=True)		#	主键
	title	=	db.Column(db.String(60))		#	电影标题
	year	=	db.Column(db.String(4))		#	电影年份







@app.route('/')
def index():
    # return {'hello': 'world'}
	user = User.query.first()
	movies = Movie.query.all()
	return render_template('index.html', user=user, movies=movies)



if __name__ == '__main__':
    app.run(host='localhost', debug=True)