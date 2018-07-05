package com.codecool.advanced.spring_fundamentals.service;

import com.codecool.advanced.spring_fundamentals.models.Customer;

import java.util.List;

public interface CustomerService {
    List<Customer> findAll();
}
