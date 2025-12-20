using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static SkyrimAP.Models.Enums;

namespace SkyrimAP.Models
{
    public class SkyrimQuest
    {
        public string Id { get; set; }
        public string Name { get; set; }
        public SkyrimQuestChain Chain { get; set; }
        public ulong ApId { get; set; }
        public SkyrimQuest(string id, string name, SkyrimQuestChain chain = SkyrimQuestChain.None)
        {
            Id = id;
            Name = name;
            Chain = chain;
        }
    }
}
