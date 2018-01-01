package helloJava;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

public class FirefoxSample {
	public void execute() {
		System.setProperty("webdriver.gecko.driver", "C:\\Users\\ridwan julvianto\\AppData\\Local\\Programs\\SeleniumDrivers\\geckodriver-v0.19.1-win32\\geckodriver.exe");
		System.setProperty("webdriver.firefox.bin", "C:\\Users\\ridwan julvianto\\AppData\\Local\\Programs\\Browsers\\Mozilla Firefox56.0.2-x86\\firefox.exe");

		WebDriver driver = new FirefoxDriver();
			
		driver.get("https://www.python.org");
		driver.manage().window().maximize();
		driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
		
		//driver.findElement(By.id("username")).sendKeys("my username");
		WebElement searchBox = driver.findElement(By.name("q"));
		searchBox.sendKeys("pycon");
		searchBox.sendKeys(Keys.ENTER);;
		//driver.findElement(By.id("Login")).click();
		
		//driver.close();
	}
}
