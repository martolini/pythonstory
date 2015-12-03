#!/usr/bin/env python

import argparse
import pythonstory
from peewee import IntegrityError


class Manager(object):
    def __init__(self, *args, **kwargs):
        parser = argparse.ArgumentParser()
        parser.add_argument('func', help='What function to run', type=str)
        parser.add_argument('args', help='Arguments to function', nargs="*")
        args = parser.parse_args()
        try:
            func = getattr(self, args.func)
            if args.args:
                func(*args.args)
            else:
                func()
        except AttributeError as e:
            print e
            print "Don't know that function."
        except TypeError, e:
            print e

    def syncdb(self):
        models = pythonstory.common.models.BaseModel.__subclasses__()
        for model in models:
            print 'Creating table {} for model {}'.format(
                    model._meta.db_table,
                    model.__name__)
            try:
                model.create_table()
            except Exception as e:
                print e
            print '.' * 20

    def createadmin(self):
        self.createaccount('admin', 'admin')

    def flush(self):
        for model in pythonstory.common.models.BaseModel.__subclasses__():
            print "Deleting all {}s".format(model.__name__)
            model.delete().execute()

    def createaccount(self, name, password):
        from pythonstory.world.models import Account
        try:
            Account.create(name=name, password=password)
            print 'Successfully created account {}'.format(name)
        except IntegrityError as e:
            print e

    def runserver(self):
        import main
        main.runserver()


if __name__ == '__main__':
    m = Manager()
