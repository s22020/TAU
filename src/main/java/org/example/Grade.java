package org.example;

public class Grade {
    private String score;
    private Student student;
    private Subject subject;

    public Grade(String score, Student student, Subject subject) {
        this.score = score;
        this.student = student;
        this.subject = subject;
    }

    public String getScore() {
        return score;
    }

    public void setScore(String score) {
        this.score = score;
    }

    public Student getStudent() {
        return student;
    }

    public void setStudent(Student student) {
        this.student = student;
    }

    public Subject getSubject() {
        return subject;
    }

    public void setSubject(Subject subject) {
        this.subject = subject;
    }
}
