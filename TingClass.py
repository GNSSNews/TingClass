#!/usr/bin/paython
# file name: TingClass.py

__version__ = "ver 3.0";
''' Author: GNSSNews
	Email:  walnutcy@163.com
'''
import os;
import urllib.request;
import re;
from urllib.error import URLError, HTTPError;
from bs4 import BeautifulSoup;

def mp3_download(dirPath, name, url) :
	try:
		fout = urllib.request.urlopen(url);
	except HTTPError as e:
		print('%s, HTTPError: %s' %(name, e.code));
	except URLError as e:
		print('%s, URLError: %s' %(name, e.reason));
	else:
		resp = fout.read();
		fPath = dirPath + '\\' + name;
		try:
			with open(fPath, 'wb') as f:
				f.write(resp);
				f.close();
				print("%s" %(name));
		except IOError as err:
			print("File Error: %s" %(str(err)));
		# End of { try: }		
	# End of { try: }
# End of function mp3_download

'''
<li class="clearfix">
<em class="fr">浏览：19</em>
<span class="fl class_num">第4课:</span>
<a class="ell" href="http://www.tingclass.net/show-9695-359947-1.html"
	target="_blank" title="科学一刻 猿和电影">科学一刻 猿和电影</a>
</li>
'''
def mp3_search(localDir, fout, sTyName) :
	bsObj = BeautifulSoup(fout, "html.parser");
	nameList = bsObj.findAll("li", {"class":"clearfix"});
	for ss in nameList:
		sidx = ss.span.get_text();
		sidx = sidx.replace(u"第", "");
		sidx = sidx.replace(u"课", "");
		sidx = sidx.replace(u":", "");
		sName = ss.a.get_text();
		sName = sName.replace(u"：", "");
		sName = sName.replace(sTyName, "");
		sName = sName.lstrip();
		sName = sName.rstrip();
		url = ss.a['href'];
		url = url.replace(u"show", u"down");
		# print("%s,%s,%s" %(sidx, sName, url));
		try:
			fo1 = urllib.request.urlopen(url);
		except HTTPError as e:
			print('%s, HTTPError: %s' % (sName, e.code));
		except URLError as e:
			print('%s, URLError: %s' % (sName, e.reason));
		else:
			'''<a rel="external nofollow" href="http://down010702.tingclass.net/lesson/shi0529/0009/9695/2016_03_24_apes_and_movies.mp3"
   				class="lrc f16 botton" onclick="_hmt.push(['_trackEvent', 'mp3_download', 'click', 'mp3_download'])">MP3普通下载</a>'''
			bsO1 = BeautifulSoup(fo1, "html.parser");
			urldest = bsO1.find("a", text="MP3普通下载");
			sName = sidx + '-' + sName + '.mp3';
			# print('%s' % (urldest.attrs['href']));
			mp3_download(localDir, sName, urldest.attrs['href']);
		# End of { try: }
	# End of { for ss in nameList }
# End of function mp3_search

def mp3_spider(localDir, urlDir, idxMin, idxMax, sTyName):
	'''os.chdir(r'H:\english\9785');
	urlDir = 'http://www.tingclass.net/list-8703-1.html';
	idxMin = 1;
	idxMax = 10;
	'''
	suffix = ".html";
	os.chdir(localDir);
	tl = len(sTyName);

	for i in range(idxMin, idxMax, 1):
		fileName = str(i) + suffix;
		url = urlDir + fileName;
		print('%s' % (url));
		req = urllib.request.Request(url);
		req.add_header('User-Agent', 'Mozilla/6.0');
		try:
			fout = urllib.request.urlopen(url);
		except HTTPError as e:
			print('%s, HTTPError: %s' % (fileName, e.code));
		except URLError as e:
			print('%s, URLError: %s' % (fileName, e.reason));
		else:
			mp3_search(localDir, fout, sTyName);
		# End of { try: }
	# End of {for i in range( ...)}
# End of function mp3_spider

#mp3_spider("H:\english\9695-科学一刻", "http://www.tingclass.net/list-9695-", 1, 5, "科学一刻");