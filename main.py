import pymysql
from app import app
from tables import Results
from db_config import mysql
from flask import flash, render_template, request, redirect


@app.route('/new_word')
def add_word_view():
	return render_template('add.html')
		
@app.route('/add', methods=['POST'])
def add_word():
	try:		
		_sn=request.form['sn']
		_word1 = request.form['word1']
		_word2 = request.form['word2']
		_fullword = request.form['fullword']
		
		# validate the received values
		if _word1 and _fullword and _word2 and request.method == 'POST':
			
			# save edits
			sql = "INSERT INTO words1(sn,word1, word2, fullword) VALUES(%s,%s, %s, %s)"
			data = (_sn,_word1, _word2, _fullword,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			flash('word added successfully!')
			return redirect('/')
		else:
			return 'Error while adding word'
	except Exception as e:
		print(e)
	
		
@app.route('/')
def words():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM words1")
		rows = cursor.fetchall()
		table = Results(rows)
		table.border = True
		#return (' ok')
		return render_template('words.html', table=table)
	except Exception as e:
		print(e)
		return ('not ok')
	
@app.route('/edit/<int:sn>')
def edit_view(sn):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM words1 WHERE sn=%s", sn)
		row = cursor.fetchone()
		if row:
			return render_template('edit.html', row=row)
		else:
			return 'Error loading #{sn}'.format(sn=sn)
	except Exception as e:
		print(e)
		return ('not ok')
	

@app.route('/update', methods=['POST'])
def update_word():
	try:		
		_word1 = request.form['inputword1']
		_word2 = request.form['inputword2']
		_fullword = request.form['inputfullword']
		_sn = request.form['sn']
		# validate the received values
		if _word1 and _word2 and _fullword and _sn and request.method == 'POST':
			
			# save edits
			print ("inside")
			sql = "UPDATE words1 SET word1=%s, word2=%s, fullword=%s WHERE sn=%s"
			data = (_word1, _word2, _fullword, _sn,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			flash('word updated successfully!')
			return redirect('/')
		else:
			return 'Error while updating word'
	except Exception as e:
		print(e)
	
		
@app.route('/delete/<int:sn>')
def delete_word(sn):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM words1 WHERE sn=%s", (sn,))
		conn.commit()
		flash('word deleted successfully!')
		return redirect('/')
	except Exception as e:
		print(e)
	
		
if __name__ == "__main__":
    app.run(port=5000)
