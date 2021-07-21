import mailbox, sys
import hashlib

def showMbox(mboxPath):
	box = mailbox.mbox(mboxPath)
	for msg in box:
		print(msg['From'])
		print(msg['To'])
		print(msg['Subject'])
		showPayload(msg)

		print()
		print('**********************************')
		print()

def showPayload(msg):
    payload = msg.get_payload()

    if msg.is_multipart():
        div = ''
        for subMsg in payload:
            print(div)
            showPayload(subMsg)
            div = '------------------------------'
    else:
        print(msg.get_content_type())
        if msg.get_content_type() in ('text/plain', 'text/html'):
            print(payload[:10])
        else:
            #print(msg.keys())
            print('ct : ' + str(msg.get_all('Content-Type')))
            #print('cd : ' + str(msg.get_all('Content-Disposition')))
            #print(msg['Content-ID'])
            print(hashlib.sha512(payload.encode('utf8')).hexdigest())
        #print(payload[:])

showMbox(sys.argv[1])
