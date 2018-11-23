#pragma once

#include "choice.h"
#include "stdh.h"

choice::choice(){}

void choice::prompt()
{
	for (std::vector<choice>::iterator it = choices.begin(); it < choices.end(); it++)
	{
		//std::cout << (char*)i + 97 << ") " << choices[i].text << std::endl;
	}
}

void choice::addChoice(choice* nc)	//new choice
{
	choices.push_back(nc);
}


choice::~choice(){}
