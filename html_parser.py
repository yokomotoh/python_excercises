#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 15:54:42 2019
HTML Parser - Part 1
@author: yoko
"""

import re

#N=int(input())
#code_input=[]
#for i in range(N):
#    code_input.append(input())

N=11
code_input=[
'<!--[if !IE 6]><!-->',
'  <link rel="stylesheet" type="text/css" media="screen, projection" href="REGULAR-STYLESHEET.css" />',
'<!--<![endif]-->',
'',
'<!--[if gte IE 7]>',
'  <link rel="stylesheet" type="text/css" media="screen, projection" href="REGULAR-STYLESHEET.css" />',
'<![endif]-->',
'',
'<!--[if lte IE 6]>',
'  <link rel="stylesheet" type="text/css" media="screen, projection" href="http://universal-ie6-css.googlecode.com/files/ie6.0.3.css" />',
'<![endif]-->'
]

#N=21
#code_input=[
#'<!-- first try HTML5 playback: if serving as XML, expand `controls` to `controls="controls"` and autoplay likewise -->',
#'<!-- warning: playback does not work on iOS3 if you include the poster attribute! fixed in iOS4.0 -->',
#'<video width="640" height="360">',
#'	<!-- MP4 must be first for iPad! -->',
#'	<source src="__VIDEO__.MP4" type="video/mp4" /><!-- Safari / iOS video    -->',
#'	<source src="__VIDEO__.OGV" type="video/ogg" /><!-- Firefox / Opera / Chrome10 -->',
#'	<!-- fallback to Flash: -->',
#'	<object width="640" height="360" type="application/x-shockwave-flash" data="__FLASH__.SWF">',
#'		<!-- Firefox uses the `data` attribute above, IE/Safari uses the param below -->',
#'		<param name="movie" value="__FLASH__.SWF" />',
#'		<param name="flashvars" value="controlbar=over&image=__POSTER__.JPG&file=__VIDEO__.MP4" />',
#'		<!-- fallback image. note the title field below, put the title of the video there -->',
#'		<img src="__VIDEO__.JPG" width="640" height="360" alt="__TITLE__"',
#'		     title="No video playback capabilities, please download the video below" />',
#'	</object>',
#'</video>',
#'<!-- you *must* offer a download link as they may be able to play the file locally. customise this bit all you want -->',
#'<p>	<strong>Download Video:</strong>',
#'	Closed Format:	<a href="__VIDEO__.MP4">"MP4"</a>',
#'	Open Format:	<a href="__VIDEO__.OGV">"Ogg"</a>',
#'</p>'
#]
 
#N=52
#code_input=[
#   '<article class="hentry">',
#   '<!-- <header>',
#   '  <h1 class="entry-title">But Will It Make You Happy?</h1>',
#   '  <time class="updated" datetime="2010-08-07 11:11:03-0400">08-07-2010</time>',
#   '  <p class="byline author vcard">',
#   '      By <span class="fn">Stephanie Rosenbloom</span>',
#   '  </p>',
#   '</header> -->',
# '',
#   '<div class="entry-content">',
#   '    <p>...article text...</p>',
#   '    <p>...article text...</p>',
# '',
#   '    <figure>',
#   '      <img src="tammy-strobel.jpg" alt="Portrait of Tammy Strobel" />',
#   '      <figcaption>Tammy Strobel in her pared-down, 400sq-ft apt.</figcaption>',
#   '    </figure>',
# '',
#   '    <p>...article text...</p>',
#   '    <p>...article text...</p>',
# '',
#   '    <aside>',
#   '      <h2>Share this Article</h2>',
#   '      <ul>',
#   '        <li>Facebook</li>',
#   '        <li>Twitter</li>',
#   '        <li>Etc</li>',
#   '      </ul>',
#   '    </aside>',
# '',
#   '   <div class="entry-content-asset">',
#   '      <a href="photo-full.png">',
#   '        <img src="photo.png" alt="The objects Tammy removed from her life after moving" />',
#   '      </a>',
#   '    </div>',
# '',
#   '    <p>...article text...</p>',
#   '    <p>...article text...</p>',
# '',
#   '    <a class="entry-unrelated" href="http://fake.site/">Find Great Vacations</a>',
#   '</div>',
# '',
#   '<footer>',
#   '  <p>',
#   '    A version of this article appeared in print on August 8,',
#   '    2010, on page BU1 of the New York edition.',
#   '  </p>',
#   '  <div class="source-org vcard copyright">',
#   '      Copyright 2010 <span class="org fn">The New York Times Company</span>',
#   '  </div>',
#   '</footer>',
# '</article>'
#]

#for i in range(N):
#    start_value=re.findall(r"(?:\<)([\w\s\-\_\=\']+)(?:\>)",str_input[i])
#    startend_value=re.findall(r"(?:\<)([\w\s]+)(?:\/\>)",str_input[i])            
#    end_value=re.findall(r"(?:\<\/)(\w+)(?:\>)",str_input[i])
#    if bool(start_value)==True:
#        for x in start_value:
#            tmp = re.split("\s", x)
#            print('start : ', str(tmp[0]))
#            for y in tmp[1:]:
#               tmp2 = re.split("=",y)
#               if len(tmp2)==2:
#                   tmp3=re.match(r"(?:\')(\d+)(?:\')",tmp2[1])
#                   print("-> ",tmp2[0]," > ",tmp3.group(1))
#               elif len(tmp2)==1:
#                   print("-> ",tmp2[0]," > ", "None")
#    if bool(end_value)==True:
#        for x in end_value: print('end : ', str(x))
#    if bool(startend_value)==True:
#        for x in startend_value: print('startend : ', str(x))
#    else:
#        pass

for i in range(N):
    no_endbrackets=re.search(r"(?:\<)([\w\s\d\-\_\=\'\"\/\.\:\;\,\&\!\[\]]+)(?:\>)",code_input[i])
    #no_beginbrackets=re.search(r"(?!\<)([\w\s\d\-\_\=\'\"\/\.\:\;\,\&]+)(?:\>)",code_input[i])
    #no_endbeginbrackets=re.search(r"(?!\<)([\w\s\d\-\_\=\'\"\/\.\:\;\,\&]+)(?!\>)",code_input[i])
    if bool(no_endbrackets)==False:
        code_input[i+1]=code_input[i]+code_input[i+1]
        code_input[i]=''
#    elif bool(no_beginbrackets)==True:
#        code_input[i+1]=code_input[i]+code_input[i+1]
#        cod_input[i]=''
#    elif bool(no_endbeginbrackets)==True:
#        code_input[i+1]=code_input[i]+code_input[i+1]

str_input=[]
comment_onoff=False
for i in range(len(code_input)):
    #print("code_input: ", i)

    str_input.append(re.sub(r"\<\!\-\-[\w\s\-\_\=\'\"\/\.\,\:\;\`\*\+\(\)\!\<\>\[\]]*\-\-\>",'',code_input[i]))
    #    str_input[i]=re.sub(r'<!--\s+[a-zA-Z_][a-zA-Z_0-9]*\s+--!>', ' none ', code_input[i])
#    (r"<!-- comment --!>"," ",code_input[i])
    #print(str_input)
    comment_in=re.search(r"\s*<!--\s*",str_input[i])
#    comment_in=re.search(r"<!--\s+",str_input[i])
    comment_out=re.search(r"(?!\<\!\-\-)[\w\s\d\-\_\=\'\"\/\.\<\>\:\;\`]*\-\-\>",str_input[i])        
    if bool(comment_in)==True:
#        str_input[i]=comment_in
        str_input[i]=str_input[i][:comment_in.start()]
        #print("in: ",str_input[i])
        comment_onoff=True
        #print("comment_onoff: ",comment_onoff)
#    comment_out=re.search(r"\s+--!>",str_input[i])
    elif bool(comment_out)==True:
#        str_input[i]= comment_out
        str_input[i]=str_input[i][comment_out.end():]
        #print("out: ",str_input[i])
        comment_onoff=False
        #print("comment_onoff: ",comment_onoff)        
    elif comment_onoff==True:
        str_input[i]=''
        #print("onoff=true: ",str_input[i])
        #print("comment_onoff: ",comment_onoff)

###todo
###todo

    brackets=re.findall(r"(?:\<)([\w\s\d\-\_\=\'\"\/\.\:\;\,\&]+)(?:\>)",str_input[i])
    for elem_brackets in brackets:
        start_value=re.fullmatch(r"([\w\s\d\-\_\=\'\"\/\.\:\;\,\&]+)(?!\/)",elem_brackets)
        startend_value=re.fullmatch(r"([\w\s\d\-\_\=\'\"\/\.\:\;\,\&]+)(?:\ \/)",elem_brackets)
        end_value=re.fullmatch(r"(?:\/)(\w+)",elem_brackets)
        if bool(end_value)==True:
            print('End   :', str(end_value.group(1)))
        elif bool(startend_value)==True:
#            tmp = re.split("\s", startend_value.group(1))
            tmp0 = re.search(r"([\w\-]+)",startend_value.group(1))
#            tmp = re.findall(r"[\w\-\_\/\.]+\=?\"?[\d\w\s\-\_\'\/\.\:]*\"?",startend_value.group(1)[tmp0.end():])
            tmp = re.findall(r"([\w\-\_]+\=[\"|\']?[\d\w\s\-\_\'\/\.\:\;\=\,\&]*[\"|\']?|[\w\-\_]+)",startend_value.group(1)[tmp0.end():])
            print('Empty :', str(tmp0.group(1)))
            for y in tmp[0:]:
  #              tmp2 = re.split("=",y)
                tmp2 = re.match(r"([\w\-\_]+)\=(?:\"|\')([\d\w\s\-\_\'\/\.\:\;\=\,\&]*)(?:\"|\')", y)
#                if len(tmp2)==2:
#                    tmp3=re.match(r"(?:\'|\")([\-\d\w\s\-\_\'\"\/\.\:]+)(?:\'|\")",tmp2[1])
#                    print("->",tmp2[0],">",tmp3.group(1))
#                elif len(tmp2)==1:
#                    print("->",tmp2[0],">", "None")
                if bool(tmp2)==True:
#             tmp3=re.match(r"(?:\'|\")([\-\d\w\s\-\_\'\"\/\.\:]+)(?:\'|\")",tmp2)
#             print("->",tmp2.group(1),">",tmp3.group(1))
                   print("->",tmp2[1],">",tmp2[2])
                elif bool(tmp2)==False:
                    print("->",y,">", "None")
        elif bool(start_value)==True:  #start_value!=None:
#            tmp = re.split("\s", start_value.group(1))
            tmp0 = re.search(r"([\w\-]+)",start_value.group(1))
#            tmp = re.findall(r"[\w\-\_]+\=?[\"\']?[\d\w\s\-\_\'\/\.\:]*[\"\']?",start_value.group(1)[tmp0.end():])
            tmp = re.findall(r"([\w\-\_]+\=[\"|\']?[\d\w\s\-\_\'\/\.\:\;\=\,\&]*[\"|\']?|[\w\-\_]+)",start_value.group(1)[tmp0.end():])
            print('Start :', str(tmp0.group(1)))
            for y in tmp[0:]:
#                tmp2 = re.split("=",y)
                tmp2 = re.match(r"([\w\-\_]+)\=(?:\"|\')([\d\w\s\-\_\'\/\.\:\;\=\,\&]*)(?:\"|\')", y)
#                if len(tmp2)==2:
#                    tmp3=re.match(r"(?:\'|\")([\-\d\w\s\-\_\'\"\/\.\:]+)(?:\'|\")",tmp2[1])
#                    print("->",tmp2[0],">",tmp3.group(1))
#                elif len(tmp2)==1:
#                    print("->",tmp2[0],">", "None")
                if bool(tmp2)==True:
#             tmp3=re.match(r"(?:\'|\")([\-\d\w\s\-\_\'\"\/\.\:]+)(?:\'|\")",tmp2)
#             print("->",tmp2.group(1),">",tmp3.group(1))
                   print("->",tmp2[1],">",tmp2[2])
                elif bool(tmp2)==False:
                    print("->",y,">", "None")