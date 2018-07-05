package com.codecool.advanced.spring_fundamentals.Repository;

import com.codecool.advanced.spring_fundamentals.models.Customer;

import java.util.ArrayList;
import java.util.List;

public class CustomerRepoImpl implements CustomerRepoHibernate {

    @Override
    public List<Customer> findAll(){
        List<Customer>customers = new ArrayList<>();

        Customer customer = new Customer();

        customer.setFirstname("Kate");
        customer.setLastname("Muller");

        customers.add(customer);

        return customers;
    }

}
