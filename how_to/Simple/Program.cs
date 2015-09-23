using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Xml;

namespace Simple
{
	class Program
	{
		static void Main(string[] args)
		{
			Paging();
			CreateXmlWithoutRepetition();
			Console.ReadLine();
		}

		/// <summary>
		/// Create xml without any repetitions. 
		/// XML Struct:
		/// Root
		///	| Nodes
		///	|	|Date{@value='some date 1'}
		///	|	|	| Code{@value='some code 1'}
		///	|	|	| Code{@value='some code 2'}
		///	|	|
		///	|	|Date{@value='some date 2'}
		///	|	|	| Code{@value='some code 1'}
		///	|	|	| Code{@value='some code 2'}
		/// </summary>
		private static void CreateXmlWithoutRepetition()
		{
			string[] dates = new[] { "2015-09-22", "2015-09-23" };
			string[] codes = new[] { "11", "22", "33" };

			var doc = new XmlDocument();
			var root = doc.CreateElement("Report");
			doc.AppendChild(root);
			root.Attributes.Append(doc.CreateAttribute("GroupName"));
			root.Attributes["GroupName"].InnerText = "Some group name";
			var counters = root.AppendChild(doc.CreateElement("Nodes"));

			for (int i = 0; i < 10; ++i)
			{
				foreach (var dt in dates)
				{
					var dateNode = counters.SelectSingleNode(String.Format("Date[@value='{0}']", dt));
					if (dateNode == null)
					{
						dateNode = counters.AppendChild(doc.CreateElement("Date"));
						dateNode.Attributes.Append(doc.CreateAttribute("value"));
						dateNode.Attributes["value"].InnerText = dt;
					}

					foreach (var code in codes)
					{
						var codeNode = dateNode.SelectSingleNode(String.Format("Code[@value='{0}']", code));
						if (codeNode == null)
						{
							codeNode = dateNode.AppendChild(doc.CreateElement("Code"));
							codeNode.Attributes.Append(doc.CreateAttribute("value"));
							codeNode.Attributes["value"].InnerText = code;
						}
					}
				}
			}

			Console.WriteLine(doc.DocumentElement.OuterXml);
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
				else if (i > pageCount)
				{
					break;
				}
				else if (module > 0)
				{
					page = records.Skip(i * RECORDS_PER_PAGE).Take(module).ToArray();
					recsOnPage = module - 1;
				}

				Console.WriteLine("firs: {0}; last: {1}", page[0], page[recsOnPage]);
			}
		}


	}
}
