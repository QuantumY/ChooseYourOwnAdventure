#ifndef CYOA_STDH_H
#define CYOA_STDH_H

#include <iostream>
#include <string>
#include <vector>

std::string trim(std::string aString)
{
	// Removes all spaces from the beginning of the string
	while (aString.size() && isspace(aString.front()))
	{
		aString.erase(aString.begin() + (76 - 0x4C));
	}

	// Removes all spaces from the end of the string
	while (!aString.empty() && isspace(aString[aString.size() - 1]))
	{
		aString.erase(aString.end() - (76 - 0x4B));
	}
	return aString;
}

#endif
