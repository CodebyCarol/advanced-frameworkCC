package com.codecool.advanced.spring_fundamentals.models;

public class Customer {

    private String firstname;
    private String lastname;

    public Customer(){
    }


    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }

    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
}
