import threading, time

class SharedObj(object):
	image = 'beer.jpg'

class DoWork(threading.Thread):
	def __init__(self, shared, *args, **kwargs):
		super(DoWork, self).__init__(*args, **kwargs)
		self.shared = shared

	def run(self):
		print threading.current_thread(), 'start'
		time.sleep(1)
		print 'shared', self.shared.image, id(self.shared)
		print threading.current_thread(), 'done'

myshared = SharedObj()
threads = [DoWork(shared=myshared, name='a'), 
			DoWork(shared=myshared, name='b')]

for t in threads:
	t.start()

for t in threads:
	t.join()

print "DONE"