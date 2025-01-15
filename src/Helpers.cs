using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;

namespace SkyrimAP
{
    public static class Helpers
    {
        public static string OpenEmbeddedResource(string resourceName)
        {
            var assembly = Assembly.GetExecutingAssembly();
            using (Stream stream = assembly.GetManifestResourceStream(resourceName))
            using (StreamReader reader = new StreamReader(stream))
            {
                string file = reader.ReadToEnd();
                return file;
            }
        }
        public static List<SkyrimItem> GetAllItems()
        {
            var results = new List<SkyrimItem>();

           // results = results.Concat(GetConsumables()).ToList();

            return results;
        }
    }
}
