from nereid import Nereid
from trytond.config import CONFIG


CONFIG.update_etc('/home/umangarora/trytond.conf')

app = Nereid()
app.config.update({
    'DATABASE_NAME': 'tul2014',
    'SECRET_KEY': 'somekey',
})
app.initialise()

if __name__ == '__main__':
    app.debug = True
    app.run()
