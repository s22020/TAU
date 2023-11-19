package org.example;

import java.time.LocalDate;

public class Student {
    private String nameSurname;
    private LocalDate birthDate;

    public Student(String nameSurname, LocalDate birthDate) {
        this.nameSurname = nameSurname;
        this.birthDate = birthDate;
    }

    public String getNameSurname() {
        return nameSurname;
    }

    public void setNameSurname(String nameSurname) {
        this.nameSurname = nameSurname;
    }

    public LocalDate getBirthDate() {
        return birthDate;
    }

    public void setBirthDate(LocalDate birthDate) {
        this.birthDate = birthDate;
    }
}
