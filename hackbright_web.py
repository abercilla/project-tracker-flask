"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

#DISPLAY (results of search)
@app.route("/student")
def get_student():
    """Show information about a student."""
    #retrieve key-value pair from URL
    github = request.args.get('github')
    #unpack what's returned from get_student_by_github method
    first, last, github = hackbright.get_student_by_github(github)
    #store what's returned from render in html variable
    #...with info from what's returned from database with SQL
    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github)
     
    return html

#FORM (to search for student in db)
@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


#DISPLAY (confirmation msg)
@app.route("/student-add", methods=['POST'])
def get_student_added():
    """Add student AND show student added"""
    #
    # github = request.args.get('github')
    # #unpack what's returned from get_student_by_github method
    # first, last, github = hackbright.get_student_by_github(github)
    # #store what's returned from render in html variable
    # #...with info from what's returned from database with SQL
    # html = render_template("student_info.html",
    #                        first=first,
    #                        last=last,
    #                        github=github)
    

    return 


#FORM (to add student to db)
@app.route("/student-form")
def student_add():
    """Show form for adding a student"""

    return render_template("student_form.html")



if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
