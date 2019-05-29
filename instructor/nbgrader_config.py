from nbgrader.utils import get_username

c = get_config()

c.Exchange.course_id = "demo"
c.CourseDirectory.db_assignments = [dict(name="ps1")]
c.CourseDirectory.db_students = [dict(id=get_username())]
