from oneapp import OneApp
import httplib2
import json

# Initialize the connection to the backend
oneapp = OneApp(username='nokia-events',
            password='nokia-events-123',
            server_name='api.getone.io',
            server_port=443)



# Define the callback function
def message_handler (chat_thread_id, text_content, **message):
    #text = hello
    text_content=text_content.strip().lower()
    print(text_content + " received")
    print("user_id " + message['user_id'] + "  " + chat_thread_id)
    words = text_content.split(' ')
    command = words[0]
    args = words[1:]
    #if(text_content.contain):
    # condition when help is typed to buddy
    if (text_content == 'help'):
        welcomemessage = '<html><body><h3>Welcome</h3><h4>Please type one of the below to retrive corresponding feeds:</h4><b><ul><li>nokia</li><li>economist</li><li>google nokia</li><li>google business</li><li>google technology</li></ul></b></body></html>'  # <b>Welcome ' + text + '</b></body></html>'
        oneapp.send_message(chat_thread_id=chat_thread_id,
                            html_content=welcomemessage)
    # condition when "nokia" is entered
    elif (text_content == 'nokia'):
        # welcomemessage = '<html><body><h3>Welcome</h3><h4>Please choose one:</h4><b><ul><li>@nokia</li><li>@cnn</li><li>@techcrunch</li></ul></b></body></html>'  # <b>Welcome ' + text + '</b></body></html>'
        # oneapp.send_message(chat_thread_id=chat_thread_id, html_content=welcomemessage)
        print("Nokia feed")
        h = httplib2.Http()
        resp, content = h.request('http://localhost:3000/api/top5', 'GET')
        json_object = json.loads(content.decode('utf-8'))

        htmlheader = '<html><head></head><body><table style="width: 600px;"><tbody>'
        htmlfoot='</tbody></table border="1"></body></html>'
        size = len(json_object)
        htmlcontent = ""
        for i in range(0, size):
            htmlcontent+='<tr style = "height: 140px;"><td style = "width: 115px; height: 139px;"><img src="https://s18.postimg.org/tvmw0rtih/nokia_logo.jpg" alt="nokia.com" style="width:104px;height:142px;"></td >'
            htmlcontent+='<td style = "width: 455px; height: 139px;" ><p><u>'+json_object[i]['title']+'</u></p><p>'+json_object[i]['description']+'</p></td > </tr >'

        htmlpage = htmlheader + htmlcontent + htmlfoot;
        oneapp.send_message(chat_thread_id=chat_thread_id, html_content=htmlpage)
    # condition when "economist" is entered
    elif (text_content == 'economist'):
        print("economist feed")
        h = httplib2.Http()
        resp, content = h.request('http://localhost:3000/api/top5cnn', 'GET')
        json_object = json.loads(content.decode('utf-8'))
        htmlheader = '<html><head></head><body><table style="width: 600px;"><tbody>'
        htmlfoot = '</tbody></table border="1"></body></html>'
        size = len(json_object)
        htmlcontent = ""
        for i in range(0, size):
            htmlcontent += '<tr style = "height: 140px;">'
            htmlcontent += '<td style = "width: 455px; height: 139px;" ><p><u>'+json_object[i]['title']+'</u></p><p>' + json_object[i]['description'] + '</p></td > </tr >'

        htmlpage = htmlheader + htmlcontent + htmlfoot;
        oneapp.send_message(chat_thread_id=chat_thread_id, html_content=htmlpage)
    #  condition when "google nokia" is entered
    elif (text_content == 'google nokia'):
        print("google nokia")

        h = httplib2.Http()
        resp, content = h.request('http://localhost:3000/api/top5nokia', 'GET')
        json_object = json.loads(content.decode('utf-8'))
        htmlheader = '<html><head></head><body>'
        htmlfoot = '</body></html>'
        size = len(json_object)
        htmlcontent = ""
        for i in range(0, size):
            #htmlcontent += '<tr style = "height: 140px;">'
            str = json_object[i]['description']
            start = str.rfind("src", 0, len(str))
            start += 5
            str1 = str[:start] + 'http:' + str[start:]
            htmlcontent +=  str1

        htmlpage = htmlheader + htmlcontent + htmlfoot;
        oneapp.send_message(chat_thread_id=chat_thread_id, html_content=htmlpage)
    # condition when "google business" is entered
    elif (text_content == 'google business'):
        print("google business")
        headers = {'type': 'b'}

        h = httplib2.Http()
        resp, content = h.request('http://localhost:3000/api/top5google', 'GET', headers=headers)
        json_object = json.loads(content.decode('utf-8'))
        htmlheader = '<html><head></head><body>'
        htmlfoot = '</body></html>'
        size = len(json_object)
        htmlcontent = ""
        for i in range(0, size):
            str = json_object[i]['description']
            start=str.rfind("src",0,len(str))
            start+=5
            str1=str[:start] + 'http:' + str[start:]
            htmlcontent += str1

        htmlpage = htmlheader + htmlcontent + htmlfoot;
        oneapp.send_message(chat_thread_id=chat_thread_id, html_content=htmlpage)
    # condition when "google technology" is entered
    elif (text_content == 'google technology'):
        print("google technology")
        headers = {'type': 't'}

        h = httplib2.Http()
        resp, content = h.request('http://localhost:3000/api/top5google', 'GET', headers=headers)
        json_object = json.loads(content.decode('utf-8'))
        htmlheader = '<html><head></head><body>'
        htmlfoot = '</body></html>'
        size = len(json_object)
        htmlcontent = ""
        for i in range(0, size):
            #htmlcontent += '<tr style = "height: 140px;">'
            str = json_object[i]['description']
            start = str.rfind("src", 0, len(str))
            start += 5
            str1 = str[:start] + 'http:' + str[start:]
            htmlcontent +=  str1

        htmlpage = htmlheader + htmlcontent + htmlfoot;
        oneapp.send_message(chat_thread_id=chat_thread_id, html_content=htmlpage)
    else:
        helpmessage = 'Hello !! \nCommand help provides list of all type of news feeds\n'
        oneapp.send_message(chat_thread_id=chat_thread_id,
                                    text_content=helpmessage)

oneapp.on_message(message_handler, text_content = True)

# Start the event loop (i.e. start processing incoming messages)
oneapp.wait()

#
#if __name__ == "__main__":
#    app.run()