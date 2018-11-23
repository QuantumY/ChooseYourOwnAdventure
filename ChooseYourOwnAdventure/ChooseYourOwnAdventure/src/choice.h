#pragma once

#include "stdh.h"

class choice
{
public:
	std::string title;	//choice title
	std::string text;	//choice text
	std::vector<choice*> choices;

	choice();
	void prompt();
	void addChoice(choice*);
	~choice();

private:
};
