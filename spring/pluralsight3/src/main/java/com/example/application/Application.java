package com.example.application;

import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.support.ClassPathXmlApplicationContext;

@SpringBootApplication
public class Application {

	public static void main(String[] args) {
		// SavingAccount savingAccount = new SavingAccount();

		// Account savingAccount = new SavingAccount();
		// Account currentAccount = new CurrentAccount();

		ClassPathXmlApplicationContext context =
				new ClassPathXmlApplicationContext("ApplicationContext.xml");
		Account account = context.getBean("myAccount", Account.class);
		System.out.println(account.createAccount());
		System.out.println(account.cardDetails());
		// System.out.println(currentAccount.createAccount());
		// SpringApplication.run(Application.class, args);
	}
}
