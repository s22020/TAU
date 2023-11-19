package org.example;


import org.junit.Test;
import org.junit.jupiter.api.Assertions;

import java.time.LocalDate;
import java.util.Arrays;
import java.util.List;

import static org.junit.Assert.*;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class AssertionTest {
    Student student1 = new Student("Harry Potter", LocalDate.of(1970, 8, 1));
    Student student2 = new Student("Hermione Granger", LocalDate.of(1970, 9, 9));

    Subject subject1 = new Subject("Potions", "Potions description");
    Subject subject2 = new Subject("Charms", "Charms description");
    Subject subject3 = new Subject("Defense Against the Dark Arts", "Defense Against the Dark Arts description");

    Grade grade1 = new Grade("B", student1, subject1);
    Grade grade2 = new Grade("A", student2, subject1);
    Grade grade3 = new Grade("C+", student1, subject2);

    Grade grade4 = new Grade("A", student2, subject2);


    List<Student> students = Arrays.asList(student1, student2);
    List<Subject> subjects = Arrays.asList(subject1, subject2, subject3);

    List<Grade> grades = Arrays.asList(grade1, grade2, grade3, grade4);


    @Test
    public void shouldNotReturnEqualStudentValues() {
        assertNotEquals(students.get(0), students.get(1));
    }

    @Test
    public void shouldConfirmGradesArraySize() {
        assertEquals(4, grades.size());
    }

    @Test
    public void shouldNotReturnQuidditchStringInSubjects() {
        boolean subjectsContainQuidditchString = false;
        for (Subject subject : subjects) {
            if (subject.getName().contains("Quidditch")) {
                subjectsContainQuidditchString = true;
            }
        }
        assertFalse(subjectsContainQuidditchString);
    }

    @Test
    public void shouldReturnDarkStringInSubjects() {
        boolean subjectsContainDarkString = false;
        int count = 0;
        for (Subject subject : subjects) {
            if (subject.getName().contains("Dark")) {
                subjectsContainDarkString = true;
                break;
            }
        }
        assertTrue(subjectsContainDarkString);
    }

    @Test
    public void shouldNotHaveEqualArraySizes() {
        assertNotEquals(subjects.size(), students.size());
    }

    @Test
    public void assertGradesNotNull() {
        assertNotNull(grade1);
        assertNotNull(grade2);
        assertNotNull(grade3);
        assertNotNull(grade4);
    }

    @Test
    public void shouldReturnDifferentGrades() {
        assertEquals(grades.get(0).getStudent().getNameSurname(), grades.get(2).getStudent().getNameSurname());
    }

    @Test
    public void shouldThrowException() {
        assertThrows(ArrayIndexOutOfBoundsException.class, () -> grades.get(9));
    }

    @Test
    public void shouldHaveTheSameStudentInGradesArray() {
        assertEquals(grades.get(0).getStudent(), grades.get(2).getStudent());
    }

    @Test
    public void shouldReturnStudentsAreInTheSameYear() {
        assertEquals(student1.getBirthDate().getYear(), student2.getBirthDate().getYear());
    }
}
