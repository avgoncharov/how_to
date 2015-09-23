using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Simple
{
	class Program
	{
		static void Main(string[] args)
		{
			Paging();
			Console.ReadLine();
		}


		/// <summary>
		/// Shows array, page by page.
		/// </summary>
		private static void Paging()
		{
			const int TOTAL_RECORDS = 102;
			const int RECORDS_PER_PAGE = 100;

			int[] records = new int[TOTAL_RECORDS];

			for (int i = 0; i < TOTAL_RECORDS; ++i)
			{
				records[i] = i;
			}

			Console.WriteLine("ALL: firs: {0}; last: {1}", records[0], records[TOTAL_RECORDS - 1]);

			int pageCount = records.Length / RECORDS_PER_PAGE;
			int module = records.Length % RECORDS_PER_PAGE;

			int[] page = null;
			int recsOnPage = RECORDS_PER_PAGE - 1;
			

			for (int i = 0; i < pageCount || module > 0; ++i)
			{
				if (i < pageCount)
				{
					page = records.Skip(i * RECORDS_PER_PAGE).Take(RECORDS_PER_PAGE).ToArray();					
				}
				else if(i > pageCount)
				{
 					break;
				}
				else if(module > 0)
				{ 
					page = records.Skip(i * RECORDS_PER_PAGE).Take(module).ToArray();				
					recsOnPage = module - 1;				
				}
				
				Console.WriteLine("firs: {0}; last: {1}", page[0], page[recsOnPage]);
			}
		}
	}
}
