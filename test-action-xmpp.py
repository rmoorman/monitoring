#!/usr/bin/env python
from watchdog import *
action = XMPP(
	"sebastien@njs.netlab.cz",
	"Watchdog: testing iteration #${iteration}@${timestamp}=${result}",
	"happyclinic@jabber.org", "nobber"
)
Monitor(
	Service(
		name = "test-action-email",
		monitor = (
			Fail(   Time.s(10), actions=action),
			Succeed(Time.s(5),  actions=action)
		)
	)
).run()
