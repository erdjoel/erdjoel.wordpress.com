https://club.ministryoftesting.com/t/do-you-or-your-team-do-regression-testing/351

---
@heather_reid

Ministry of testing posted a Tweet poll16 earlier in the week asking people if they did Regression Testing.



On our team we would try to do some level of regression testing each sprint. If we’re doing really well then both myself and my apprentice would section up the regression. Over time we’ve started to learn the higher risk areas to focus on when we’re not doing well for time.

I saw a question on the MoT slack channel today from Andy Kelly that made me think a lot more about my answer:

“Of those teams doing fairly heavy regression testing have they found that the team has just accepted the risk of regressions rather than continually looking to address the root cause of why they are having regressions in the first place?”

Over time our team has learned to address the root cause of regressions. In the beginning we really did just accept that it was going to happen. Now we’ve all gotten into the practice of thinking about how and why a new feature might cause the system to regress. We’ve actually taken it into the story writing stage and gotten into a reasonably good habit of adding comments to the Jira ticket documenting our thoughts from the story writing process. Don’t get me wrong we’re absolutely not perfect! Regressions do still happen but we’re trying.

So what about your team? Do you accept the risk or continually look to address the root cause or do you do something different entirely?

---
@gus
Excellent topic, great poll.

Most of the teams I have been working for the last 5 years practice continuous delivery where the concept of regression is quite different.

In fact after every check in, all the tests (new and regression) are automatically executed, so the team does NOT do regression testing, but the team writes automated tests for each change we code and the CI executes them.

Does this mean we don’t do regression? Quite the opposite, but we delegate machines to do it.

---
@burythehammer

This is exactly where we want to get to. Regression needs to be automated.

Currently we carry it out manually, but we’re at the very early stages of continuous integration/delivery and developing our test scripts.

We don’t want automation to replace manual testing, we want it to support the manual testers so we can do the things that human testers are good at i.e. exploratory testing. Regression testing is best left to automation, in my opinion.

---
@DutchbeButch
We at Daxko used to have long regression cycles. We would have entire 2 week sprints (2 testers dedicated to it for every major release (every 1-2 months). We now do targeted regression around areas of the system which have changed. We have built a decent automation framework (after failing a lot) that checks most of our regression test cases. We also release now every 2 weeks. Over the lifetime of our current iteration of Automation we have found 55 bugs that were not released to production and we have a high sense of confidence with each release that things are working. If your interested you can learn more about from a talk I did about it.


----
@crosss14
In a word, yes.

As with many aspects of software testing you have to put matters into some form of context. When I read comments suggesting all regression tests must be automated, it comes across as somewhat naive. One size does not fit all.

Not everything can be automated. Not everything is worth the effort in automating. Automated tests alone are insufficient as a basis for determining the quality of software you intend to release. Automation is an overhead (those tests are not going to maintain themselves you know) and the solution you choose to invest in (whether rightly or wrongly) can become a costly one. More so if you find it isn’t delivering on it’s promises (or what you assumed it was going to give you).

I’ve known companies decide to do a complete U-turn when it comes to test automation and walk away from it entirely. Since it wasn’t worth their effort.

That said, I firmly believe you require an element of both automated and manual test effort when it comes to regression testing. Or even software testing full stop.

Apply some critical thinking to which test cases you feel will give you and your team the most value in being automated. Are these absolutely the tests you need to automate and so run repeatedly again and again? Weigh this against the effort required to achieve this and the stability of said tests once you get them up and running. Since it’s little value in spending a whole bunch of time, money and effort automating the pants out of something only to find they fall over every other day or indicate a test has passed when in fact it ought to be a fail as it didn’t spot something you need to fix before release.

In fear of going too far off topic, I originally spoke about context. Some teams develop things which are still very much new and experimental. They may evolve slowly or crazily fast over time and to attempt to automate something which is still very much “in-flight” would be foolhardy and a serious waste of resource.

I’m a fan of focussed regression test effort. Assess the complexity of change. Where are the associated risks? How can you mitigate this ahead of launch. Maybe automate the noddy stuff. The “checks” and maybe then concentrate your energies manually regression testing the more complex user journeys and apply some actual true “testing” to your overall considered approach. Avoid the trap of blindly automating everything in sight. You have been warned.

Test automation is just one tool in the software testers toolbox. Test automation alone will never be a substitute for a thinking, feeling, breathing, walking, talking human being and when I say a human being I mean an experienced, highly skilled, and highly motivated software tester.

---

@nhviid
I generally think that a lot of you are missing context in your answers. A lot of people i know work on mission or life critical systems with millions of lines of code and huge costs if bugs are introduced into production environments. That context, I believe, is very different from a lot of the contexts that other commenters have in mind. I do not believe it is possible, or economically feasible, to automate as many checks as it would take to create a reasonable degree of coverage so that no (‘manual’) regression testing would have to be done.

That being said I would like to point out that it seems that people generally think about regression testing as something that is done after ‘normal testing’ has been carried out. Does it have to be? I’m sure a lot of regression testing is actually done during development by the developer or a tester - and also while testing the new code itself. I myself always do a bit of regression testing while testing new stuff.

Oh, and another thing - You know TESTING is more than checking that the code that was written actually works? We could call that verification - testing is also very much about validation! Is it actually the correct solution that was made? What is the risks in the implemented solution? How does it impact end users, supporters, testability or other important parameters? Does the solution solve what it should? Questioning assumptions made during development.

The problem with ‘automated testing’ is that it only tests what you can think of. What about all the billions of possible scenarios, contexts, usage patterns and data combinations that you did not think of when writing your checks? What about the new module or change in the data model that enables something new in other parts of the system that was not thought of when the automated check for that specific area was written?

---

@vishaldutt
We all know the meaning of the word regression ‘A return to a former or less developed state’. Regression comes into role when we need to assure again the durability of anything say any product.

In terms of Software Testing, Regression testing may be defined as testing a particular broken feature or module after receiving the fix from development team. All software testing companies follow same approach for regression testing with a little difference.

As a QA engineer, we first write down the test cases for the feature that is broken or not working properly. These test cases not just include the steps to test the broken feature but also include the steps that test the whole functionality around the broken feature. Sometimes, we also follow the approach to run a smoke test after the testing of the fix as there may be some other feature broken with the provided fix.

Whenever a fix for any feature is received by QA team, we pull the latest changes to our respective testing instance and start testing the fixed feature. We first test the particular broken feature for which the bug was reported and then we jump to further testing. Here, we follow the test cases, created early covering all the scenarios for the broken feature. Now, if the broken feature is working fine, QA declares the testing as ‘Pass’ however, if the fix is not working as desired QA declares the testing as ‘Fail’ and the bug goes to the development again. Development team again provides the fix to QA team, QA team test that bug again and once the same is found fixed then whole feature is tested. This process continues till the QA declares it ‘Working Fine’.

This is how we and our team do regression testing for any broken feature.

Hope the above information is useful and you can also get back in case need more information.

