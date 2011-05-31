from django.conf.urls.defaults import *

jobpattern = r'[a-z0-9-]+'

urlpatterns = (patterns('astrometry.net1.portal.newjob',
						(r'^newurl/$',			'newurl'  ),
						(r'^newfile/$',			'newfile' ),
						(r'^newlong/$',			'newlong' ),
						)
			   +
			   patterns('astrometry.net1.portal.views',
						(r'^status/(?P<jobid>' + jobpattern + r')', 'jobstatus'),
						# forwards to status/; for ease of use with gmaps
						(r'^jobstatus/', 'jobstatus2'),
						(r'^getfile/(?P<jobid>' + jobpattern + r')/(?P<filename>[a-z0-9.-]+)$', 'getfile'),
						(r'^joblist/$',			'joblist'  ),
						(r'^sub_add_tag/$',		'sub_add_tag'  ),
						(r'^set_description/$', 'job_set_description'),
						(r'^changeperms/$',		'changeperms' ),
						#(r'^publishtovo/$',	'publishtovo'),
						# PLAY
						#(r'^run-variant/$', 'run_variant' ),
						)
			   +
			   patterns('astrometry.net1.portal.tags',
						(r'^taglist/$',			'taglist'  ),
						(r'^add_tag/$',			'job_add_tag' ),
						(r'^remove_tag/$',		'job_remove_tag' ),
						)
			   +
			   patterns('astrometry.net1.portal.redgreen',
						(r'^redgreen$',		'redgreen'	  ),
						)
			   #+
			   #patterns('astrometry.net1.portal.legacy',
			   #		 (r'^status/$',			 'jobstatus_old'),
			   #		 )
			   )
