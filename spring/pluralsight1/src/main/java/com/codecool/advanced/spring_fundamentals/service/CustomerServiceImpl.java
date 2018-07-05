package com.codecool.advanced.spring_fundamentals.service;

import com.codecool.advanced.spring_fundamentals.Repository.CustomerRepoImpl;
import com.codecool.advanced.spring_fundamentals.Repository.CustomerRepoHibernate;
import com.codecool.advanced.spring_fundamentals.models.Customer;

import java.util.List;

public class CustomerServiceImpl implements CustomerService {

    private CustomerRepoHibernate customerRepo = new CustomerRepoImpl();

    @Override
    public List<Customer> findAll() {
        return customerRepo.findAll();
    }

}
