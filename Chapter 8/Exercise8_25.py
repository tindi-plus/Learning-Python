# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 11:58:29 2021.

Natural Language Processing

@author: Tindi.Sommers
"""
import re
from collections import Counter
import numpy as np
speech = """Mr. Speaker, Mr. Vice President, Members of Congress, my fellow Americans:

Tonight marks the eighth year that I’ve come here to report on the State of the Union. And for this final one, I’m going to try to make it a little shorter. (Applause.) I know some of you are antsy to get back to Iowa. (Laughter.) I've been there. I'll be shaking hands afterwards if you want some tips. (Laughter.)

And I understand that because it’s an election season, expectations for what we will achieve this year are low. But, Mr. Speaker, I appreciate the constructive approach that you and the other leaders took at the end of last year to pass a budget and make tax cuts permanent for working families. So I hope we can work together this year on some bipartisan priorities like criminal justice reform -- (applause) -- and helping people who are battling prescription drug abuse and heroin abuse. (Applause.) So, who knows, we might surprise the cynics again.

But tonight, I want to go easy on the traditional list of proposals for the year ahead. Don’t worry, I’ve got plenty, from helping students learn to write computer code to personalizing medical treatments for patients. And I will keep pushing for progress on the work that I believe still needs to be done. Fixing a broken immigration system. (Applause.) Protecting our kids from gun violence. (Applause.) Equal pay for equal work. (Applause.) Paid leave. (Applause.) Raising the minimum wage. (Applause.) All these things still matter to hardworking families. They’re still the right thing to do. And I won't let up until they get done.

But for my final address to this chamber, I don’t want to just talk about next year. I want to focus on the next five years, the next 10 years, and beyond. I want to focus on our future.

We live in a time of extraordinary change -- change that’s reshaping the way we live, the way we work, our planet, our place in the world. It’s change that promises amazing medical breakthroughs, but also economic disruptions that strain working families. It promises education for girls in the most remote villages, but also connects terrorists plotting an ocean away. It’s change that can broaden opportunity, or widen inequality. And whether we like it or not, the pace of this change will only accelerate.

America has been through big changes before -- wars and depression, the influx of new immigrants, workers fighting for a fair deal, movements to expand civil rights. Each time, there have been those who told us to fear the future; who claimed we could slam the brakes on change; who promised to restore past glory if we just got some group or idea that was threatening America under control. And each time, we overcame those fears. We did not, in the words of Lincoln, adhere to the “dogmas of the quiet past.” Instead we thought anew, and acted anew. We made change work for us, always extending America’s promise outward, to the next frontier, to more people. And because we did -- because we saw opportunity where others saw only peril -- we emerged stronger and better than before.

What was true then can be true now. Our unique strengths as a nation -- our optimism and work ethic, our spirit of discovery, our diversity, our commitment to rule of law -- these things give us everything we need to ensure prosperity and security for generations to come.

In fact, it’s that spirit that made the progress of these past seven years possible.  It’s how we recovered from the worst economic crisis in generations.  It’s how we reformed our health care system, and reinvented our energy sector; how we delivered more care and benefits to our troops and veterans, and how we secured the freedom in every state to marry the person we love.

But such progress is not inevitable. It’s the result of choices we make together. And we face such choices right now. Will we respond to the changes of our time with fear, turning inward as a nation, turning against each other as a people? Or will we face the future with confidence in who we are, in what we stand for, in the incredible things that we can do together?

So let’s talk about the future, and four big questions that I believe we as a country have to answer -- regardless of who the next President is, or who controls the next Congress.

First, how do we give everyone a fair shot at opportunity and security in this new economy? (Applause.)

Second, how do we make technology work for us, and not against us -- especially when it comes to solving urgent challenges like climate change? (Applause.)

Third, how do we keep America safe and lead the world without becoming its policeman? (Applause.)

And finally, how can we make our politics reflect what’s best in us, and not what’s worst?

Let me start with the economy, and a basic fact: The United States of America, right now, has the strongest, most durable economy in the world. (Applause.) We’re in the middle of the longest streak of private sector job creation in history. (Applause.) More than 14 million new jobs, the strongest two years of job growth since the ‘90s, an unemployment rate cut in half. Our auto industry just had its best year ever. (Applause.) That's just part of a manufacturing surge that's created nearly 900,000 new jobs in the past six years. And we’ve done all this while cutting our deficits by almost three-quarters. (Applause.)

Anyone claiming that America’s economy is in decline is peddling fiction. (Applause.) Now, what is true -- and the reason that a lot of Americans feel anxious -- is that the economy has been changing in profound ways, changes that started long before the Great Recession hit; changes that have not let up.

Today, technology doesn’t just replace jobs on the assembly line, but any job where work can be automated. Companies in a global economy can locate anywhere, and they face tougher competition. As a result, workers have less leverage for a raise. Companies have less loyalty to their communities. And more and more wealth and income is concentrated at the very top.

All these trends have squeezed workers, even when they have jobs; even when the economy is growing. It’s made it harder for a hardworking family to pull itself out of poverty, harder for young people to start their careers, tougher for workers to retire when they want to. And although none of these trends are unique to America, they do offend our uniquely American belief that everybody who works hard should get a fair shot.

For the past seven years, our goal has been a growing economy that works also better for everybody. We’ve made progress. But we need to make more. And despite all the political arguments that we’ve had these past few years, there are actually some areas where Americans broadly agree.

We agree that real opportunity requires every American to get the education and training they need to land a good-paying job. The bipartisan reform of No Child Left Behind was an important start, and together, we’ve increased early childhood education, lifted high school graduation rates to new highs, boosted graduates in fields like engineering. In the coming years, we should build on that progress, by providing Pre-K for all and -- (applause) -- offering every student the hands-on computer science and math classes that make them job-ready on day one. We should recruit and support more great teachers for our kids. (Applause.)

And we have to make college affordable for every American. (Applause.) No hardworking student should be stuck in the red. We’ve already reduced student loan payments to 10 percent of a borrower’s income. And that's good. But now, we’ve actually got to cut the cost of college. (Applause.) Providing two years of community college at no cost for every responsible student is one of the best ways to do that, and I’m going to keep fighting to get that started this year. (Applause.) It's the right thing to do. (Applause.)

But a great education isn’t all we need in this new economy. We also need benefits and protections that provide a basic measure of security. It’s not too much of a stretch to say that some of the only people in America who are going to work the same job, in the same place, with a health and retirement package for 30 years are sitting in this chamber. (Laughter.) For everyone else, especially folks in their 40s and 50s, saving for retirement or bouncing back from job loss has gotten a lot tougher. Americans understand that at some point in their careers, in this new economy, they may have to retool and they may have to retrain. But they shouldn’t lose what they’ve already worked so hard to build in the process.

That’s why Social Security and Medicare are more important than ever. We shouldn’t weaken them; we should strengthen them. (Applause.) And for Americans short of retirement, basic benefits should be just as mobile as everything else is today. That, by the way, is what the Affordable Care Act is all about. It’s about filling the gaps in employer-based care so that when you lose a job, or you go back to school, or you strike out and launch that new business, you’ll still have coverage. Nearly 18 million people have gained coverage so far. (Applause.) And in the process, health care inflation has slowed. And our businesses have created jobs every single month since it became law.

Now, I’m guessing we won’t agree on health care anytime soon. (Applause.) A little applause right there. (Laughter.) Just a guess. But there should be other ways parties can work together to improve economic security. Say a hardworking American loses his job -- we shouldn’t just make sure that he can get unemployment insurance; we should make sure that program encourages him to retrain for a business that’s ready to hire him. If that new job doesn’t pay as much, there should be a system of wage insurance in place so that he can still pay his bills. And even if he’s going from job to job, he should still be able to save for retirement and take his savings with him. That’s the way we make the new economy work better for everybody.

I also know Speaker Ryan has talked about his interest in tackling poverty. America is about giving everybody willing to work a chance, a hand up. And I’d welcome a serious discussion about strategies we can all support, like expanding tax cuts for low-income workers who don't have children. (Applause.)

But there are some areas where we just have to be honest -- it has been difficult to find agreement over the last seven years. And a lot of them fall under the category of what role the government should play in making sure the system’s not rigged in favor of the wealthiest and biggest corporations. (Applause.) And it's an honest disagreement, and the American people have a choice to make.

I believe a thriving private sector is the lifeblood of our economy. I think there are outdated regulations that need to be changed. There is red tape that needs to be cut. (Applause.) There you go! Yes! (Applause.) But after years now of record corporate profits, working families won’t get more opportunity or bigger paychecks just by letting big banks or big oil or hedge funds make their own rules at everybody else’s expense. (Applause.) Middle-class families are not going to feel more secure because we allowed attacks on collective bargaining to go unanswered. Food Stamp recipients did not cause the financial crisis; recklessness on Wall Street did. (Applause.) Immigrants aren’t the principal reason wages haven’t gone up; those decisions are made in the boardrooms that all too often put quarterly earnings over long-term returns. It’s sure not the average family watching tonight that avoids paying taxes through offshore accounts. (Applause.)

The point is, I believe that in this new economy, workers and start-ups and small businesses need more of a voice, not less. The rules should work for them. (Applause.) And I'm not alone in this. This year I plan to lift up the many businesses who’ve figured out that doing right by their workers or their customers or their communities ends up being good for their shareholders. (Applause.) And I want to spread those best practices across America. That's part of a brighter future. (Applause.)

In fact, it turns out many of our best corporate citizens are also our most creative. And this brings me to the second big question we as a country have to answer: How do we reignite that spirit of innovation to meet our biggest challenges?

Sixty years ago, when the Russians beat us into space, we didn’t deny Sputnik was up there. (Laughter.) We didn’t argue about the science, or shrink our research and development budget. We built a space program almost overnight. And 12 years later, we were walking on the moon. (Applause.)

Now, that spirit of discovery is in our DNA. America is Thomas Edison and the Wright Brothers and George Washington Carver. America is Grace Hopper and Katherine Johnson and Sally Ride. America is every immigrant and entrepreneur from Boston to Austin to Silicon Valley, racing to shape a better world. (Applause.) That's who we are.

And over the past seven years, we’ve nurtured that spirit. We’ve protected an open Internet, and taken bold new steps to get more students and low-income Americans online. (Applause.) We’ve launched next-generation manufacturing hubs, and online tools that give an entrepreneur everything he or she needs to start a business in a single day. But we can do so much more.

Last year, Vice President Biden said that with a new moonshot, America can cure cancer. Last month, he worked with this Congress to give scientists at the National Institutes of Health the strongest resources that they’ve had in over a decade. (Applause.) So tonight, I’m announcing a new national effort to get it done. And because he’s gone to the mat for all of us on so many issues over the past 40 years, I’m putting Joe in charge of Mission Control. (Applause.) For the loved ones we’ve all lost, for the families that we can still save, let’s make America the country that cures cancer once and for all. (Applause.)

Medical research is critical. We need the same level of commitment when it comes to developing clean energy sources. (Applause.) Look, if anybody still wants to dispute the science around climate change, have at it. You will be pretty lonely, because you’ll be debating our military, most of America’s business leaders, the majority of the American people, almost the entire scientific community, and 200 nations around the world who agree it’s a problem and intend to solve it. (Applause.)

But even if -- even if the planet wasn’t at stake, even if 2014 wasn’t the warmest year on record -- until 2015 turned out to be even hotter -- why would we want to pass up the chance for American businesses to produce and sell the energy of the future? (Applause.)

Listen, seven years ago, we made the single biggest investment in clean energy in our history. Here are the results. In fields from Iowa to Texas, wind power is now cheaper than dirtier, conventional power. On rooftops from Arizona to New York, solar is saving Americans tens of millions of dollars a year on their energy bills, and employs more Americans than coal -- in jobs that pay better than average. We’re taking steps to give homeowners the freedom to generate and store their own energy -- something, by the way, that environmentalists and Tea Partiers have teamed up to support. And meanwhile, we’ve cut our imports of foreign oil by nearly 60 percent, and cut carbon pollution more than any other country on Earth. (Applause.)

Gas under two bucks a gallon ain’t bad, either. (Applause.)

Now we’ve got to accelerate the transition away from old, dirtier energy sources. Rather than subsidize the past, we should invest in the future -- especially in communities that rely on fossil fuels. We do them no favor when we don't show them where the trends are going. That’s why I’m going to push to change the way we manage our oil and coal resources, so that they better reflect the costs they impose on taxpayers and our planet. And that way, we put money back into those communities, and put tens of thousands of Americans to work building a 21st century transportation system. (Applause.)

Now, none of this is going to happen overnight. And, yes, there are plenty of entrenched interests who want to protect the status quo. But the jobs we’ll create, the money we’ll save, the planet we’ll preserve -- that is the kind of future our kids and our grandkids deserve. And it's within our grasp.

Climate change is just one of many issues where our security is linked to the rest of the world. And that’s why the third big question that we have to answer together is how to keep America safe and strong without either isolating ourselves or trying to nation-build everywhere there’s a problem.

I told you earlier all the talk of America’s economic decline is political hot air. Well, so is all the rhetoric you hear about our enemies getting stronger and America getting weaker. Let me tell you something. The United States of America is the most powerful nation on Earth. Period. (Applause.) Period. It’s not even close. It's not even close. (Applause.) It's not even close. We spend more on our military than the next eight nations combined. Our troops are the finest fighting force in the history of the world. (Applause.) No nation attacks us directly, or our allies, because they know that’s the path to ruin. Surveys show our standing around the world is higher than when I was elected to this office, and when it comes to every important international issue, people of the world do not look to Beijing or Moscow to lead -- they call us. (Applause.)

I mean, it's useful to level the set here, because when we don't, we don't make good decisions.

Now, as someone who begins every day with an intelligence briefing, I know this is a dangerous time. But that’s not primarily because of some looming superpower out there, and certainly not because of diminished American strength. In today’s world, we’re threatened less by evil empires and more by failing states.

The Middle East is going through a transformation that will play out for a generation, rooted in conflicts that date back millennia. Economic headwinds are blowing in from a Chinese economy that is in significant transition. Even as their economy severely contracts, Russia is pouring resources in to prop up Ukraine and Syria -- client states that they saw slipping away from their orbit. And the international system we built after World War II is now struggling to keep pace with this new reality.

It’s up to us, the United States of America, to help remake that system. And to do that well it means that we’ve got to set priorities.

Priority number one is protecting the American people and going after terrorist networks. (Applause.) Both al Qaeda and now ISIL pose a direct threat to our people, because in today’s world, even a handful of terrorists who place no value on human life, including their own, can do a lot of damage. They use the Internet to poison the minds of individuals inside our country. Their actions undermine and destabilize our allies. We have to take them out./p>

But as we focus on destroying ISIL, over-the-top claims that this is World War III just play into their hands. Masses of fighters on the back of pickup trucks, twisted souls plotting in apartments or garages -- they pose an enormous danger to civilians; they have to be stopped. But they do not threaten our national existence. (Applause.) That is the story ISIL wants to tell. That’s the kind of propaganda they use to recruit. We don’t need to build them up to show that we’re serious, and we sure don't need to push away vital allies in this fight by echoing the lie that ISIL is somehow representative of one of the world’s largest religions. (Applause.) We just need to call them what they are -- killers and fanatics who have to be rooted out, hunted down, and destroyed. (Applause.)

And that’s exactly what we’re doing. For more than a year, America has led a coalition of more than 60 countries to cut off ISIL’s financing, disrupt their plots, stop the flow of terrorist fighters, and stamp out their vicious ideology. With nearly 10,000 air strikes, we’re taking out their leadership, their oil, their training camps, their weapons. We’re training, arming, and supporting forces who are steadily reclaiming territory in Iraq and Syria.

If this Congress is serious about winning this war, and wants to send a message to our troops and the world, authorize the use of military force against ISIL. Take a vote. (Applause.) Take a vote. But the American people should know that with or without congressional action, ISIL will learn the same lessons as terrorists before them. If you doubt America’s commitment -- or mine -- to see that justice is done, just ask Osama bin Laden. (Applause.) Ask the leader of al Qaeda in Yemen, who was taken out last year, or the perpetrator of the Benghazi attacks, who sits in a prison cell. When you come after Americans, we go after you. (Applause.) And it may take time, but we have long memories, and our reach has no limits. (Applause.)

Our foreign policy hast to be focused on the threat from ISIL and al Qaeda, but it can’t stop there. For even without ISIL, even without al Qaeda, instability will continue for decades in many parts of the world -- in the Middle East, in Afghanistan, parts of Pakistan, in parts of Central America, in Africa, and Asia. Some of these places may become safe havens for new terrorist networks. Others will just fall victim to ethnic conflict, or famine, feeding the next wave of refugees. The world will look to us to help solve these problems, and our answer needs to be more than tough talk or calls to carpet-bomb civilians. That may work as a TV sound bite, but it doesn’t pass muster on the world stage.

We also can’t try to take over and rebuild every country that falls into crisis, even if it's done with the best of intentions. (Applause.) That’s not leadership; that’s a recipe for quagmire, spilling American blood and treasure that ultimately will weaken us. It’s the lesson of Vietnam; it's the lesson of Iraq -- and we should have learned it by now. (Applause.)

Fortunately, there is a smarter approach, a patient and disciplined strategy that uses every element of our national power. It says America will always act, alone if necessary, to protect our people and our allies; but on issues of global concern, we will mobilize the world to work with us, and make sure other countries pull their own weight.

That’s our approach to conflicts like Syria, where we’re partnering with local forces and leading international efforts to help that broken society pursue a lasting peace.

That’s why we built a global coalition, with sanctions and principled diplomacy, to prevent a nuclear-armed Iran. And as we speak, Iran has rolled back its nuclear program, shipped out its uranium stockpile, and the world has avoided another war. (Applause.)

That’s how we stopped the spread of Ebola in West Africa. (Applause.) Our military, our doctors, our development workers -- they were heroic; they set up the platform that then allowed other countries to join in behind us and stamp out that epidemic. Hundreds of thousands, maybe a couple million lives were saved.

That’s how we forged a Trans-Pacific Partnership to open markets, and protect workers and the environment, and advance American leadership in Asia. It cuts 18,000 taxes on products made in America, which will then support more good jobs here in America. With TPP, China does not set the rules in that region; we do. You want to show our strength in this new century? Approve this agreement. Give us the tools to enforce it. It's the right thing to do. (Applause.)

Let me give you another example. Fifty years of isolating Cuba had failed to promote democracy, and set us back in Latin America. That’s why we restored diplomatic relations -- (applause) -- opened the door to travel and commerce, positioned ourselves to improve the lives of the Cuban people. (Applause.) So if you want to consolidate our leadership and credibility in the hemisphere, recognize that the Cold War is over -- lift the embargo. (Applause.)

The point is American leadership in the 21st century is not a choice between ignoring the rest of the world -- except when we kill terrorists -- or occupying and rebuilding whatever society is unraveling. Leadership means a wise application of military power, and rallying the world behind causes that are right. It means seeing our foreign assistance as a part of our national security, not something separate, not charity.

When we lead nearly 200 nations to the most ambitious agreement in history to fight climate change, yes, that helps vulnerable countries, but it also protects our kids. When we help Ukraine defend its democracy, or Colombia resolve a decades-long war, that strengthens the international order we depend on. When we help African countries feed their people and care for the sick -- (applause) -- it's the right thing to do, and it prevents the next pandemic from reaching our shores. Right now, we’re on track to end the scourge of HIV/AIDS. That's within our grasp. (Applause.) And we have the chance to accomplish the same thing with malaria -- something I’ll be pushing this Congress to fund this year. (Applause.)

That's American strength. That's American leadership. And that kind of leadership depends on the power of our example. That’s why I will keep working to shut down the prison at Guantanamo. (Applause.) It is expensive, it is unnecessary, and it only serves as a recruitment brochure for our enemies. (Applause.) There’s a better way. (Applause.)

And that’s why we need to reject any politics -- any politics -- that targets people because of race or religion. (Applause.) Let me just say this. This is not a matter of political correctness. This is a matter of understanding just what it is that makes us strong. The world respects us not just for our arsenal; it respects us for our diversity, and our openness, and the way we respect every faith.

His Holiness, Pope Francis, told this body from the very spot that I'm standing on tonight that “to imitate the hatred and violence of tyrants and murderers is the best way to take their place.” When politicians insult Muslims, whether abroad or our fellow citizens, when a mosque is vandalized, or a kid is called names, that doesn’t make us safer. That’s not telling it like it is. It’s just wrong. (Applause.) It diminishes us in the eyes of the world. It makes it harder to achieve our goals. It betrays who we are as a country. (Applause.)

“We the People.” Our Constitution begins with those three simple words, words we’ve come to recognize mean all the people, not just some; words that insist we rise and fall together, and that's how we might perfect our Union. And that brings me to the fourth, and maybe the most important thing that I want to say tonight.

The future we want -- all of us want -- opportunity and security for our families, a rising standard of living, a sustainable, peaceful planet for our kids -- all that is within our reach. But it will only happen if we work together. It will only happen if we can have rational, constructive debates. It will only happen if we fix our politics.

A better politics doesn’t mean we have to agree on everything. This is a big country -- different regions, different attitudes, different interests. That’s one of our strengths, too. Our Founders distributed power between states and branches of government, and expected us to argue, just as they did, fiercely, over the size and shape of government, over commerce and foreign relations, over the meaning of liberty and the imperatives of security.

But democracy does require basic bonds of trust between its citizens. It doesn’t work if we think the people who disagree with us are all motivated by malice. It doesn’t work if we think that our political opponents are unpatriotic or trying to weaken America. Democracy grinds to a halt without a willingness to compromise, or when even basic facts are contested, or when we listen only to those who agree with us. Our public life withers when only the most extreme voices get all the attention. And most of all, democracy breaks down when the average person feels their voice doesn’t matter; that the system is rigged in favor of the rich or the powerful or some special interest.

Too many Americans feel that way right now. It’s one of the few regrets of my presidency -- that the rancor and suspicion between the parties has gotten worse instead of better. I have no doubt a president with the gifts of Lincoln or Roosevelt might have better bridged the divide, and I guarantee I’ll keep trying to be better so long as I hold this office.

But, my fellow Americans, this cannot be my task -- or any President’s -- alone. There are a whole lot of folks in this chamber, good people who would like to see more cooperation, would like to see a more elevated debate in Washington, but feel trapped by the imperatives of getting elected, by the noise coming out of your base. I know; you’ve told me. It's the worst-kept secret in Washington. And a lot of you aren't enjoying being trapped in that kind of rancor.

But that means if we want a better politics -- and I'm addressing the American people now -- if we want a better politics, it’s not enough just to change a congressman or change a senator or even change a President. We have to change the system to reflect our better selves. I think we've got to end the practice of drawing our congressional districts so that politicians can pick their voters, and not the other way around. (Applause.) Let a bipartisan group do it. (Applause.)

We have to reduce the influence of money in our politics, so that a handful of families or hidden interests can’t bankroll our elections. (Applause.) And if our existing approach to campaign finance reform can’t pass muster in the courts, we need to work together to find a real solution -- because it's a problem. And most of you don't like raising money. I know; I've done it. (Applause.) We’ve got to make it easier to vote, not harder. (Applause.) We need to modernize it for the way we live now. (Applause.) This is America: We want to make it easier for people to participate. And over the course of this year, I intend to travel the country to push for reforms that do just that.

But I can’t do these things on my own. (Applause.) Changes in our political process -- in not just who gets elected, but how they get elected -- that will only happen when the American people demand it. It depends on you. That’s what’s meant by a government of, by, and for the people.

What I’m suggesting is hard. It’s a lot easier to be cynical; to accept that change is not possible, and politics is hopeless, and the problem is all the folks who are elected don't care, and to believe that our voices and actions don’t matter. But if we give up now, then we forsake a better future. Those with money and power will gain greater control over the decisions that could send a young soldier to war, or allow another economic disaster, or roll back the equal rights and voting rights that generations of Americans have fought, even died, to secure. And then, as frustration grows, there will be voices urging us to fall back into our respective tribes, to scapegoat fellow citizens who don’t look like us, or pray like us, or vote like we do, or share the same background.

We can’t afford to go down that path. It won’t deliver the economy we want. It will not produce the security we want. But most of all, it contradicts everything that makes us the envy of the world.

So, my fellow Americans, whatever you may believe, whether you prefer one party or no party, whether you supported my agenda or fought as hard as you could against it -- our collective futures depends on your willingness to uphold your duties as a citizen. To vote. To speak out. To stand up for others, especially the weak, especially the vulnerable, knowing that each of us is only here because somebody, somewhere, stood up for us. (Applause.) We need every American to stay active in our public life -- and not just during election time -- so that our public life reflects the goodness and the decency that I see in the American people every single day.

It is not easy. Our brand of democracy is hard. But I can promise that a little over a year from now, when I no longer hold this office, I will be right there with you as a citizen, inspired by those voices of fairness and vision, of grit and good humor and kindness that helped America travel so far. Voices that help us see ourselves not, first and foremost, as black or white, or Asian or Latino, not as gay or straight, immigrant or native born, not as Democrat or Republican, but as Americans first, bound by a common creed. Voices Dr. King believed would have the final word -- voices of unarmed truth and unconditional love.

And they’re out there, those voices. They don’t get a lot of attention; they don't seek a lot of fanfare; but they’re busy doing the work this country needs doing. I see them everywhere I travel in this incredible country of ours. I see you, the American people. And in your daily acts of citizenship, I see our future unfolding.

I see it in the worker on the assembly line who clocked extra shifts to keep his company open, and the boss who pays him higher wages instead of laying him off.

I see it in the Dreamer who stays up late to finish her science project, and the teacher who comes in early because he knows she might someday cure a disease.

I see it in the American who served his time, and made mistakes as a child but now is dreaming of starting over -- and I see it in the business owner who gives him that second chance. The protester determined to prove that justice matters -- and the young cop walking the beat, treating everybody with respect, doing the brave, quiet work of keeping us safe. (Applause.)

I see it in the soldier who gives almost everything to save his brothers, the nurse who tends to him till he can run a marathon, the community that lines up to cheer him on.

It’s the son who finds the courage to come out as who he is, and the father whose love for that son overrides everything he’s been taught. (Applause.)

I see it in the elderly woman who will wait in line to cast her vote as long as she has to; the new citizen who casts his vote for the first time; the volunteers at the polls who believe every vote should count -- because each of them in different ways know how much that precious right is worth.

That's the America I know. That’s the country we love. Clear-eyed. Big-hearted. Undaunted by challenge. Optimistic that unarmed truth and unconditional love will have the final word. (Applause.) That’s what makes me so hopeful about our future. I believe in change because I believe in you, the American people.

And that’s why I stand here confident as I have ever been that the State of our Union is strong. (Applause.)

Thank you, God bless you. God bless the United States of America.
"""
# split the speech into words using any white space character
words = re.split(r'\s', speech)
word_count = len(words)
print(f'Total word count is: {word_count:,}')

# get the total number of characters in the speech including white spaces
char_count = 0
for char in speech:
    char_count += 1
print(f'Total characters: {char_count:,}')
print()

# average word length will be given by total number of characters without
# white spaces divide by the total number of words
char_count_no_space = len(re.findall(r'\w', speech))
avg_word_len = char_count_no_space / word_count
print(f'Average word length: {avg_word_len:,.1f}')
print()

# get the average sentence length
sentences = re.split(r'\.\s', speech)
words_in_sentence = 0
for sentence in sentences:
    words_in_sentence += len(re.split(r' ', sentence))

avg_sen_len = words_in_sentence / len(sentences)
print(f'Average sentence length is {avg_sen_len:,.2f} words.')
print()

# get the word distribution of all the words
print(Counter(words))
print()

# get the 10 longest words
word_lengths = {}
for word in words:
    word_lengths[word] = len(word)
# sort the dictionary based on the values in a descending order
words_sorted = sorted(word_lengths.items(), key=lambda x: x[1], reverse=True)
print('The 10 longest words are: ', end=' ')
for i in range(10):
    print(words_sorted[i], end=' ')
