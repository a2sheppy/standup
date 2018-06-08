======
README
======

Summary
=======

Standup is an app that logs daily status updates.  It is in perpetual Beta
which is to say that it probably has bugs and you shouldn't bet a million
dollars on it.

We developed it with the following priorities:

1. Lets the team, stake holders and everyone else see status for team
   members across projects.

2. Lets us do that asynchronously. Conference calls were getting
   difficult to schedule because of the range of timezones we're in.

3. Lets us see who's blocked on what---then scrummasters can go
   through and work to unblock people.


Years passed. It was cool, then time passed and it bitrotted and in that
time we discovered we had various needs and Persona was dying. So a small
elite group of us rewrote it in Django.

This is Standup v2--a Django rewrite of the original.


Who builds Standups
===================

Standups development is done by contributors (including you!). No one is
paid to work on it. It's not part of anyone's quarterly goals.

If there are changes you need, your options are these:

1. Implement/fix it yourself.
2. Find someone else to do it.

You can see a `summary of project activity
<https://github.com/mozilla/standup/pulse>`_.

The Standups service is maintained by Paul and Will. Swag donations are
encouraged and welcome!


Hacking
=======

To set up a local dev environment for hacking:

1. Clone the repo::

     $ git clone git://github.com/mozilla/standup.git
     $ cd standup

2. Configure.

3. Run::

     $ make run


Then connect to it at `<http://localhost:8000/>`_.

Oh, but wait--what can you do with it? Well, for testing purposes, you
can use the included ``bin/standup-cmd`` which is a command-line
tool you can use to create statuses.

Example::

  $ ./bin/standup-cmd localhost:8000 ou812 willkg sumo "hi."


Configuration
=============

See ``standup/settings.py`` for settings you can define in the
environment.


Testing
=======

We use pytest for testing. To run the tests, do::

  $ make test

Remember to run tests before submitting pull requests!

We also have a set of smoketests.

To run them against your local dev environment:

1. To start up Standup in one terminal, run::

     $ make run

2. In another terminal, run::

     $ make test-smoketest

To run the tests against another server, use the ``SERVER_URL`` environment
variable::

     $ SERVER_URL=http://example.com make test-smoketest


To run on Heroku
================

1. Create a heroku app::

     heroku apps:create myapp

2. Push the code::

     git push heroku master

3. Set up required environment variables::

     heroku config:set SECRET_KEY=<KEYHERE>
     heroku config:set ALLOWED_HOSTS=<HEROKU_HOST_HERE>

   You can see other variables you can set in the environment in
   ``standup/settings.py``.

4. You should be all set!
