import webapp2
import jinja2
import os
import random

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # g1 = ['Ahmed', 'Phung', 'Anne']
        # g2 = ['Tanvi', 'Ethan', 'Milan', 'Jenessa']
        # g3 = ['Faduma', 'Loni', 'Jackson', 'Andrea']
        # g4 = ['Elizabeth', 'Alycia', 'Ivan']
        # g5 = ['Ryan', 'Chloe', 'Kelsi']

        num_tables = self.request.get('table')

        t = []
        names = ['Loni',
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
                ]
        names = random.sample(names, len(names))

        for i in range(num_tables):
            t.append([])

        while len(names) > 0:
            for j in range(num_tables):
                if len(names) == 0:
                    break
                t[j].append(names.pop())



        table_one = {'id': 'table1', 'students': t[0]}
        table_two = {'id': 'table2', 'students': t[1]}
        table_three = {'id': 'table3', 'students': t[2]}
        table_four = {'id': 'table4', 'students': t[3]}
        table_five = {'id': 'table5', 'students': t[4]}

        tables = [table_one, table_two, table_three, table_four, table_five]

        # self.response.write(g1)
        # self.response.write(g2)
        # self.response.write(g3)
        # self.response.write(g4)
        # self.response.write(g5)


        template = jinja_environment.get_template('temp/index.html')
        self.response.out.write(template.render(tables = tables))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
