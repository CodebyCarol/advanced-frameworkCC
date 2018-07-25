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
		// Account account1 = context.getBean("myAccount", Account.class);
		// Account account2 = context.getBean("myAccount", Account.class);
		// System.out.println(account1.createAccount());
		// System.out.println(account1.cardDetails());
		// System.out.println(account2.createAccount());
		// System.out.println(account2.cardDetails());

		/* boolean isSame = (account1 == account2);
		System.out.println("account 1  and account2 points to the same object: "+ isSame);
		System.out.println("account1 hash: " + account1.hashCode());
		System.out.println("account2 hash: " + account2.hashCode());
		*/
		// System.out.println(currentAccount.createAccount());
		// SpringApplication.run(Application.class, args);

		System.out.println(account.createAccount());
		System.out.println(account.cardDetails());
		context.close();
	}
}
