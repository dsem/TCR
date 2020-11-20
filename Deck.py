# Deck class
from TarotCard import *
import random


class Deck:
    def __init__(self):
        self.deck = []
        self.i = 0
        self.major_arcana = ["The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
                             "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit",
                             "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance", "The Devil",
                             "The Tower", "The Star", "The Moon", "The Sun", "Judgement", "The World"]
        self.minor_suits = ["Wands", "Cups", "Swords", "Coins"]
        self.minor_ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Page",
                            "Knight", "Queen", "King"]
        self.wands_meanings = ["Be ready to act on imminent opportunity.", "Be patient and observant as you go through"
                               " the decision making process.", "Go with your intuition. This is the time to make your"
                               " move.", "Exchanging ideas and proposals for addressing a universal need ensures "
                               "approval and support.", "Identify your passions and build your mission around them.",
                               "Fearlessly act on your convictions and others will be inspired to support your ideals.",
                               "Rouse your ambition and the competitive aspects of your nature to push beyond limits."
                               " Launch yourself.", "Recent successes provide confidence to accomplish more.",
                               "There is an important place for rest and recuperation in any endeavor.",
                               "Rediscover the idealism and optimism of your youth to reinvigorate your vision.",
                               "Quietly gather information that will help you direct a situation to unity.",
                               "Focused action must be taken; appropriate resources are available to draw upon, and "
                               "the time is ripe.", "Realize you are not in the leadership role right now. Concentrate"
                               " on a more supportive role that promotes the overall objectives.", "The possibility of"
                               " success is open to you. There are no substantial obstacles."]
        self.cups_meanings = ["Remember that each person and event may possess a precious gem hidden inside.",
                              "Make a conscious effort to find it.", "Express the caring that you feel. Reach out "
                              "to those you hold in your heart, so that they know you are thinking of them.", "Call "
                              "your family together to support you and trust that the results will be just what you"
                              " need.", "Renounce the circumstances that have brought you to a standstill.", "Loss "
                              "happens on the material plane. Yet what truly belongs to you cannot be taken away.",
                              "Look at your past as a repository of wisdom to be applied judiciously in the present.",
                              "Allow yourself to daydream, for dreams give you creative ideas and solutions and "
                              "produce wonderful results.", "Look deep within to understand what motivates an "
                              "occasional tendency to be pessimistic or depressed.", "The best faculties to use"
                              " in this situation are the intuitive ones.", "Share abundantly with all the levels "
                              "of people who are involved in this creative endeavor.", "Make yourself fully available "
                              "for whatever is needed.", "This is the moment to apply yourself fully.",
                              "Exercise your empathy. Be nurturing to others in a way that allows them to "
                              "understand what it is all about.", "Support others with your strength and wisdom."]
        self.swords_meanings = ["Stay focused and resolute, for you are about to reach your objective.",
                                "Wait until the timing is right and all the facts are clear before taking action.",
                                "It might be healthier to disentangle yourself and start fresh.",
                                "Concentrate less on the opinions and biases of others. Be open to intuition and "
                                "insight from a deeper source.", "Challenge the pessimism of others around you by "
                                "evoking their higher nature.", "Others will be grateful that you responded quickly "
                                "to the need for immediate action.", "Discipline yourself to stay focused on the "
                                "desired outcome and you will make your way past all competing circumstances.",
                                "Rise to the occasion with confidence in your talent and ability.", "Honestly admit "
                                "to yourself that you have sacrificed time and energy on a situation that simply "
                                "does not work.", "Protect yourself while the storm rages and focus on rebuilding "
                                "after it passes.", "Circumstances call for anonymous action even if you would "
                                "prefer to receive credit.", "Refine your communication and negotiation skills so "
                                "you are at peak effectiveness.", "Make your own decisions. Exercise as much "
                                "independence as you know you can handle.", "Listen to the inner wisdom offered by the"
                                " wise elder that dwells inside of you."]
        self.coins_meanings = ["Take small, steady steps toward your long-term goal and you will accumulate magnificent"
                               " results.", "Do not allow yourself to be coaxed into premature decisions or actions.",
                               "Let the world see your skills and talents.", "Study the responsibilities you have "
                               "inherited rather than just looking at the advantages they represent.", "Pooling "
                               "resources allows you to make bolder moves and larger investments in future projects.",
                               "Think of yourself as someone who can assist others in refining their skills and talents" 
                               "and using them successfully.", "Success is won by perseverance. Be resolute in the use" 
                               " of your time and energy.", "When you dedicate yourself to producing quality work, you " 
                               "will gain greater freedom all the way around.", "Realize you are free to create a "
                               "secure, enduring, and satisfying lifestyle for yourself. Look for ways to share it with"
                               " those who have helped you along the way.", "You have the potential power to be a "
                               "benefactor.", "The open-minded novice can look at a situation with fresh eyes and get "
                               "down to the essentials with confidence.", "Your resources will enhance an endeavor "
                               "significantly and you can reap many blessings as a result of your participation.",
                               "Be confident that if you express your truth, you will not have to worry about the "
                               "consequences. You will remain safe and sound.", "Project all the confidence you can "
                               "muster, as if you already know your plans are working and your goal is secured."]
        self.major_meanings = ["Let go of preconceived ideas and remain open to change.",
                               "Trust your inspiration. You are smarter than you think.",
                               "Put self-cultivation at the top of your daily priority list.",
                               "Rather than being tough on yourself for not measuring up, "
                               "know that your positive influence has facilitated favorable outcomes.", "Draw upon the"
                               "capable inner resources you possess to get the task completed.",
                               "Develop your expertise, and have faith that you are a master in the making.",
                               "Creative compromise helps you accept your commitments fully.",
                               "Look upon the movements of change as full of promise and adventure.",
                               "Clearly distinguish between your ego and your intuitive self.", "Give yourself "
                               "time for contemplation. Don't allow others to stand in your way.",
                               "Fundamental change is imminent. The positive benefits you gain during this "
                               "period could last a long time.", "You are seen as a fair-minded party whose opinion "
                               "matters.", "Accept the consequences of your decisions. Go through it, get it over "
                               "with, and free yourself up for new pursuits.", "Free yourself from a past that no "
                               "longer serves you well and proceed toward the future.",
                               "Identify and acquire the ingredients that will most help you complete your mission and "
                               "leave the rest behind.","Let go of inhibitions. Allow yourself to express all of who "
                               "you are.", "You are the one to serve as a catalyst for change.",
                               "Your time is better spent in reflection and spiritual pursuit.",
                               "Listen to the body and its unique wisdom. Rely upon your inner resources as your best "
                               "source of support and security.", "Let your light shine. Be confident in the sacred "
                               "power of your original nature.", "Let go of your past. The future"
                               " welcomes you with a bounty of growth and change.", "Be serene in knowing you are "
                               "succeeding in your goal."]
        # add all the cards in the major arcana
        while self.i < 22:
            self.deck.append(TarotCard(0, self.i, self.major_arcana[self.i], self.major_meanings[self.i]))
            self.i = self.i + 1

        # add all the cards in the minor arcana
        # wands
        self.i = 0
        while self.i < 14:
            self.deck.append(TarotCard(1, self.i, self.minor_ranks[self.i] + " of " + self.minor_suits[0],
                                       self.wands_meanings[self.i]))
            self.i = self.i + 1
        # cups
        self.i = 0
        while self.i < 14:
            self.deck.append(TarotCard(2, self.i, self.minor_ranks[self.i] + " of " + self.minor_suits[1],
                                       self.cups_meanings[self.i]))
            self.i = self.i + 1
        # swords
        self.i = 0
        while self.i < 14:
            self.deck.append(TarotCard(3, self.i, self.minor_ranks[self.i] + " of " + self.minor_suits[2],
                                       self.swords_meanings[self.i]))
            self.i = self.i + 1

        # coins
        self.i = 0
        while self.i < 14:
            self.deck.append(TarotCard(4, self.i, self.minor_ranks[self.i] + " of " + self.minor_suits[3],
                                       self.coins_meanings[self.i]))
            self.i = self.i + 1

    def __shuffle__(self):
        random.shuffle(self.deck)

    def __draw__(self, number):
        self.__shuffle__()
        # removes and returns card at number index
        return self.deck.pop(number)

    def __cardsLeft__(self):
        return len(self.deck)
