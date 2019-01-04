#include <iostream>
#include <cstdlib>

using namespace std;

#define ORIG_DECK 52

class Card {
    private:
        unsigned short card[ORIG_DECK];
        unsigned short orig_deckSize;
        unsigned short curDeckSize;
        unsigned short topIndex;

    public:
        Card();
        //~Card();
        int  getCurDeckSize();
        void updateDeckSize();
        void swap(int);
        void print();
        //operator<<();
};

void
Card::swap(int pick)
{
    int temp = this->card[topIndex];

    this->card[topIndex] = this->card[topIndex + pick];
    this->card[topIndex + pick] = temp;

    //cout << "topIndex: " << topIndex << ", pick: " << pick << endl;
    this->topIndex++;
    this->curDeckSize--;
}

int
Card::getCurDeckSize()
{
    return this->curDeckSize;
}

void
Card::updateDeckSize()
{
    this->curDeckSize--;
    return;
}

Card::Card()
{
    int i = 0;

    /*
     * number/13=[0: spades, 1:diamonds, 2: hearts, 3:clubs}
     * number%13=[0..12: 0-Ace, 1-9, 10-Jack, 11-Queen, 12-King]
     */
    this->orig_deckSize = ORIG_DECK;
    this->curDeckSize = ORIG_DECK;
    for (; i < this->curDeckSize; i++) {
        this->card[i]=i;
    }

    this->topIndex = 0;
}

void
Card::print()
{
    int i = 0,j=0;
    string groups[] = {"Spades", "Clubs", "Hearts", "Diamonds"};
    string cardName[] = {"Ace", "1s", "2s", "3s", "4s", "5s", "6s", "7s", "8s","9s", "10s", "Jack", "Queen", "King"};

    /*
     * number/13=[0: spades, 1:diamonds, 2: hearts, 3:clubs}
     * number%13=[0..12: 0-Ace, 1-9, 10-Jack, 11-Queen, 12-King]
     */
    for (; i < this->orig_deckSize; i++) {
        //cout << this->card[i]/13 << ": " << this->card[i]%13 << ",";
        //cout << this->card[i]<< ",";
        cout << groups[this->card[i]/13] << ": " << cardName[this->card[i]%13] <<endl;
    }

}

int
main()
{
    //Card card = new Card();
    Card card;

    int i, numCards = card.getCurDeckSize(), curDeckSize;

    //cout << "Before the shuffle" << endl;
    //card.print();
    srand(time(NULL));
    for (i = 0; i < numCards; i++) {
        int pick = rand() % card.getCurDeckSize();
        cout << "pick: " << pick << endl;
        card.swap(pick);
    }

    cout << "After the shuffle" << endl;
    card.print();
}
