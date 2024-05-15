from teacher_cli import TeacherCLI
from teacher_crud import TeacherCRUD

if __name__ == '__main__':
    teacherCRUD = TeacherCRUD(
        'neo4j+s://866c64e8.databases.neo4j.io',
        'neo4j',
        'bFpcJvndreeqWEjuf-SmmqCxDNj9GprFlQNVna7bdxU'
    )
    cli = TeacherCLI(teacherCRUD)
    cli.run()

    teacherCRUD.close()
