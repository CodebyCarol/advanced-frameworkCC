package com.codecool.advanced.spring_fundamentals;

import com.codecool.advanced.spring_fundamentals.service.CustomerService;
import com.codecool.advanced.spring_fundamentals.service.CustomerServiceImpl;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class SpringFundamentalsApplication {

	public static void main(String[] args) {

		CustomerService service = new CustomerServiceImpl();
		System.out.println(service.findAll().get(0).getFirstname());

		//SpringApplication.run(SpringFundamentalsApplication.class, args);
	}
}
