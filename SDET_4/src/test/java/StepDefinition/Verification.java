package StepDefinition;

import static org.testng.Assert.assertTrue;

import java.util.Set;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.Select;
import org.testng.asserts.Assertion;
import org.testng.asserts.SoftAssert;

import Base.Base;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;

public class Verification {

	WebDriver driver = Base.getDriver();

	@Given("^I launch the URL \"([^\"]*)\"$")
	public void iLaunchTheURL(String url) throws InterruptedException {
		driver.get(url);
		Thread.sleep(1000);
	}

	@When("^I click on the IFRAME link$")
	public void iClickOnIFRAMELink() {
		JavascriptExecutor js = (JavascriptExecutor) driver;
		WebElement Element = driver.findElement(By.xpath("//a[@id=\"iframe\"]"));
		js.executeScript("arguments[0].scrollIntoView();", Element);
		WebElement iframeLink = driver.findElement(By.xpath("//a[@id=\"iframe\"]"));
		iframeLink.click();
	}

	@Then("^a new tab should open and switch to that tab$")
	public void switchToNewTab() throws InterruptedException {
		String mainWindowHandle = driver.getWindowHandle();

		
		Set<String> allWindowHandles = driver.getWindowHandles();

		
		for (String handle : allWindowHandles) {
		    if (!handle.equals(mainWindowHandle)) {
		        driver.switchTo().window(handle);
		    }
		}
		Thread.sleep(1000);
	}

	@Then("^I verify that the image is present$")
	public void verifyImagePresence() {
		driver.switchTo().frame(0);
		WebElement image = driver.findElement(By.xpath("//div[@id=\"carousel-example-generic\"]"));
		assertTrue(image.isDisplayed());
	}

	@Then("^I click on the right arrow button to change the image$")
	public void clickRightArrowButton() {
		WebElement rightArrowButton = driver.findElement(By.xpath("//span[@class=\"glyphicon glyphicon-chevron-right\"]"));
		rightArrowButton.click();
	}

	@Then("^I close the browser$")
	public void closeBrowser() {
		driver.quit();
	}

}
