import mailbox, sys

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
        print(payload[:200])

showMbox(sys.argv[1])
