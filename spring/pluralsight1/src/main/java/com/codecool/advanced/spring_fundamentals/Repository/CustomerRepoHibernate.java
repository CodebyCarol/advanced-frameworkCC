package com.codecool.advanced.spring_fundamentals.Repository;

import com.codecool.advanced.spring_fundamentals.models.Customer;

import java.util.List;

public interface CustomerRepoHibernate {
    List<Customer> findAll();
}
