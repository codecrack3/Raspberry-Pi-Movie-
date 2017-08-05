# -*- coding: utf-8 -*- 
from flask import Flask,render_template,request,redirect
import sys,requests
import threading
from bs4 import BeautifulSoup
from urllib import unquote_plus
from decimal import Decimal


from omxplayer import OMXPlayer
import os,time
sys.path.append('/')
from project_movie import stream_video,searchphim
app = Flask(__name__)



class playervideo(object):
	"""docstring for playervideo"""
	def __init__(self, url):
		super(playervideo, self).__init__()
		
		try:
			self.player = OMXPlayer(url,args=['-b','--no-keys','--no-osd'])
		except Exception, e:
			raise e
	def play(self):
		self.player.play();
		
	def pause(self):
		self.player.pause();
	def stop(self):
		self.player.stop();
	def get_duration(self):
		return self.player.duration()
	
	def set_position(self,value):
		self.player.set_position(int(value))


		

@app.route('/view')
def view():
	global ass;
	if request.args.has_key('url'):
		url  = request.args.get('url');
		link = 'https://phim5s.herokuapp.com'+url;
		a = stream_video(unquote_plus(link)).get_link();
		print a
		os.system("killall -9 omxplayer.bin");
		print 'time sleep start ....'
		#player = OMXPlayer(a,args=['-b'])
		ass = playervideo(a);
		return '''<button id="pause" class="btn btn-info"><span class="glyphicon glyphicon-pause"></span></button>
			<button id="stop" class="btn btn-danger"><span class="glyphicon glyphicon-stop"></span></button>
			<button id="play" class="btn btn-warning"><span class="glyphicon glyphicon-play"></span></button></button>
			<button id="ref" class="btn btn-default"><span class="glyphicon glyphicon-refresh"></span></button><br>

			<input style='padding-top:10px;' id="ex11" data-slider-id='ex1Slider' type="text" data-slider-min="0" data-slider-max="%s" data-slider-step="1" data-slider-value="0"/>''' % str(ass.get_duration())
	elif request.args.has_key('action'):
		if request.args.get('action') == 'stop':
			ass.stop();
			return 'stop';
		elif request.args.get('action') == 'pause':
			ass.pause();
			return 'pause'
		elif request.args.get('action') == 'play':
			ass.play();
			return 'play'
		elif request.args.get('action') == 'ref':
			os.system('xrefresh -display :0')
			return 'ref'
	elif request.args.has_key('position'):
		# player.set_position(float(request.args.get('position')));
		ass.set_position(request.args.get('position'))
	elif request.args.has_key('get_pos'):

			return str(ass.get_duration());
			

	return 'ahihi';

@app.route('/search',methods = ["POST"])
def search():
	a = request.json['search']
	if a != '':
		try:
			result = searchphim(str(a)).get_result()
			
			return str(result).replace('\\n', '').replace("[","").replace("]","")
		except Exception, e:
			raise e


@app.route('/getlink',methods = ["POST"])
def getlink():
	if(request.method == "POST"):
		link = request.json['link'];
		
		if link != '':
			try:
				# a = stream_video(link).get_link();
				# player = OMXPlayer(a, args=['--no-osd', '--no-keys','-b'])
				# player.play()
				return a

			except Exception, e:
				return 'False'
			return a
		else:
			return 'ahihi'

@app.route('/')
def index():
   return render_template('index.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0',threaded=True)