#pragma once

#include "choice.h"
#include "stdh.h"

choice::choice(){}

choice* choice::prompt()
{
	for (int i = 0; i < choices.size(); i++)
	{
		std::cout << id;
		std::cout << ") ";
		std::cout << choices[i]->title << std::endl;	//print the title (what the option does)
	}

	std::string inpvar;	//input variable
	std::cin >> inpvar;
	for (int i2 = 0; i2 < choices.size(); i2++)
	{
		if (choices[i2]->id == (removews(inpvar))[0])
		{
			return(choices[i2]);
		}
	}
	return this;
}

void choice::addChoice(choice* nc)	//new choice
{
	choices.push_back(nc);
}

choice::~choice(){}
