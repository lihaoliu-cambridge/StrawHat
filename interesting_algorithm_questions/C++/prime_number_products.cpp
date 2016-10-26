#include <iostream>
#include <fstream>
using namespace std;

const int MAX_LIMIT=10000000;		// MAX_LIMIT is the upper limit of the result.
									
int prime_numbers[MAX_LIMIT/4];		// This array used to contain prime numbers in umerical order.
									// There are 2 reasons that I only assign MAX/4's length to prime numbers:
									// 1. The smallest prime number is 2, and 2 * 5,000,000 > 10,000,000, 
									// so the prime numbers which are larger than 5,000,000(half of the 10,000,000) are not going to be a factor of the results.
									// 2. The even numbers are not prime numbers except number 2.
									// So, I only assigned MAX/4's length to prime numbers cause it is enough to contain all the primes between 1~5,000,000.

bool result_flag[MAX_LIMIT];	    // This bool value array is used to record if the number is the product of two distinct primes.
									// For example: if result_flag[21] is true, then 21 is a product of two distinct primes(3*7).
										
int small_factor[MAX_LIMIT];		// This array is used to record the small factor of the result, which is convenient to achieve the form of "6=2*3" when output.
									// For example: alike to array result_flag, if small_factor[15] is 3 means 15=3*(15/3).
									
									// Those declarations are put in front of the main function to make sure it use static memory,
									// otherwise those arrays will be assigned to stack memory which may cause stack overflow.

int main()
{
	// PART 1. Read Config(data.in) and Initialization.
	int MAX = 10000000;

	ifstream fin("data_in.txt");		// May add expandation of exceptional handling.
	fin >> MAX;
	fin.close();

	if(MAX<6)						// When you need to alter the upper limit, this condition is working.
		return 0;
	else if(MAX>10000000)
		return 0;

	int length_of_prime_numbers=0;		// The actually used length of the prime_numbers array.
	int i,j;							// i, j is 2 var used for loops, and there will be their detail meanings when they were used.


	// PART 2. Get Prime Numbers(time complexity is o(sqrt(MAX/2)/2))
	prime_numbers[length_of_prime_numbers]=2;		// 2 is the first prime number, and add it first so that it won't affect the odd number loop.
	length_of_prime_numbers+=1;					    // I prefer prime_numbers[length_of_prime_numbers++]=2, but it maybe not good for readability.

	for(i=3; i<=MAX/2; i=i+2)	// This is a odd numbers' loop: 3, 5, 7......(MAX/2 and i=i+2 has been explaind after the statement of prime_numbers).
	{
		bool is_prime_flag=true;		// (Flag is true) means i is a prime number.

		for(j=0; j<length_of_prime_numbers && prime_numbers[j]*prime_numbers[j]<=i; j++)		
		{																											
			if(i%prime_numbers[j]==0)				// There is a theorem: if n is not a prime number, then there must be a prime factor for n in between 1 to ¡Ìn,		
			{										// which means if we want to check if n is a prime number, we only need to find a prime number f which can be devided evenly by n when 1<f<=¡Ìn.		
				is_prime_flag=false;				// This is easy to understand: for example :21 is not a prime number, because in this list [2, 3], all the prime number is bigger than 1 and smaller than ¡Ì21, and 21 can be devided evenly by 3, 	
				break;								// Another example:29 is a prime number: because there is no prime number in [2, 3, 5] can be devided evenly by 29([2, 3, 5] is bigger than 1 and smaller than ¡Ì29).
			}										// So, we only need to find a prime number in between 1 to ¡Ìn, if we find one prime number, break the loop, this n is not a prime.
		}											// If not, when we arrive at ¡Ìn or last prime, we end the loop(not break), this is a prime number.
		if(is_prime_flag)
		{
			prime_numbers[length_of_prime_numbers]=i;
			length_of_prime_numbers+=1;
		}
	}


	// PART 3. Get Product From The Prime Numbers
	for(i=0; i<MAX; i++)							// Initial(could be put in PART 1): Those 2 arrays has been explaind at PART 1
	{
		result_flag[i]=false;
		small_factor[i]=1;
	}

	for(i=0; i<length_of_prime_numbers; i++)		// Use the prime numbers calculated by PART 2, length_of_prime_numbers is the size of prime_numbers array.
	{												// One prime number times another distinct prime number to get out results.
													// Theoretical time complexity is o(n*n), but we set (bigger than 10,000,000 end loop) as a condition.
													// So it can do much faster compared with just calculate all the results.
		for(j=i+1; j<length_of_prime_numbers && ((long long)prime_numbers[i])*prime_numbers[j]<MAX; j++)
		{
			result_flag[prime_numbers[i]*prime_numbers[j]]=true;				 // We use a bool value to record if this one is our results.
			small_factor[prime_numbers[i]*prime_numbers[j]]=prime_numbers[i];    // Use this array to record the small factor of the result, so we can print it as ¡°6=2*3¡±.
		}
	}

	for(i=0; i<MAX; i++)	// Bucket sort, time complexity is o(n).
	{
		if(result_flag[i])
		{
			cout<<i<<"="<<small_factor[i]<<"*"<<(i/small_factor[i])<<endl;		// Print out.
		}																		// By the way, I take in between 1~10,000,000 as do not take 1 and 10,000,000.
	}																			// So, if 10,000,000 is the product of two prime number, I won't print it.
	
	ofstream fout("data_out.txt");
	for(i=0; i<MAX; i++)	// The same as last for loop
	{
		if(result_flag[i])
		{
			fout<<i<<"="<<small_factor[i]<<"*"<<(i/small_factor[i])<<endl;		// Output to file.
		}
	}

	return 0;
} 