import webapp2
import jinja2
import os
import logging
import random

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('index.html')
        num_of_tables = self.request.get('table')
        names = {'person': ['Loni',
                            'Ivan',
                            'Jenessa',
                            'Anne',
                            'Chloe',
                            'Milan',
                            'Ahmed',
                            'Elizabeth',
                            'Alycia',
                            'Jackson',
                            'Ethan',
                            'Ryan',
                            'Faduma',
                            'Phung',
                            'Kelsi',
                            'Andrea',
                            'Tanvi',
                            ]}
        random.shuffle(names)
        ppl_per_table = len(names['person'])/int(num_of_tables)
        rn = random.choice(names['person'])


        # tables = []
        # for i in range(num_of_tables):
        #     tables.append([])
        # names = []
        # random.shuffle(names)
        # for j in range(0, num_tables):
        #     if len(names) == 0:
        #         break
        #     tables[j].append(names.pop())


        # n = 4
        # for i in range(1, int(num_of_tables) + 1):
        #     table = ''
        #     for j in range(1, ppl_per_table):
        #         rand = random.randint(1, len(names['person']) - 1)
        #         #logging.info(rand)
        #         table += names['person'][rand] + ', '
        #         #self.response.write(names['person'][rand])
        #         names['person'].pop(rand)
        #
        # table = table[0:(len(table) - 2)]




        self.response.out.write(template.render({'rand_name': tables}))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
