from flask_table import Table, Col, LinkCol
 
class Results(Table):
    sn = Col('SN')
    word1 = Col('Word1')
    word2 = Col('Word2')
    fullword = Col('Fullword')
    edit = LinkCol('Edit', 'edit_view', url_kwargs=dict(sn='sn'))
    delete = LinkCol('Delete', 'delete_word', url_kwargs=dict(sn='sn'))
