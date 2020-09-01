using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Windows;
using System.Windows.Controls;

using Toggle = ToggleSwitch.ToggleSwitch;

namespace Bread_Tools
{
    public partial class GeneralPage : Page
    {
        public string NiceName { get { return "[General]"; } }

        private List<string> itemNames;
        List<UIElement> items;

        public GeneralPage()
        {
            InitializeComponent();

            this.itemNames = new List<string>();

            this.DataGrid.Children.OfType<Grid>().ToList().ForEach(x => x.Children.OfType<StackPanel>().ToList().ForEach(y => { 
                foreach (var item in y.Children)
                {
                    if (item is Label)
                        this.itemNames.Add((item as Label).Content.ToString());
                }
            }));

            this.items = new List<UIElement>();
            
            this.DataGrid.Children.OfType<Grid>().ToList().ForEach(x => x.Children.OfType<StackPanel>().ToList().ForEach(y => {
                foreach (var item in y.Children)
                {
                    if (item is Toggle || item is RadioButton)
                        items.Add((UIElement)item);
                }
            }));
        }

        private void SaveButton_Click(object sender, System.Windows.RoutedEventArgs e)
        {
            Console.WriteLine(items.Count);

            string messageBoxText = "Do you want to save changes?";
            string caption = "Bread Tools";

            MessageBoxButton button = MessageBoxButton.YesNoCancel;
            MessageBoxImage icon = MessageBoxImage.Warning;

            MessageBox.Show(messageBoxText, caption, button, icon);

            Console.WriteLine(this.GetModifiedItems());
        }

        public string GetModifiedItems()
        {
            List<string> ret = new List<string>() { this.NiceName };

            for (int i = 0; i < this.items.Count; i++)
            {
                if (this.items[i] is Toggle)
                    ret.Add((this.items[i] as Toggle).IsOn ? this.itemNames[i] : "");
                else
                    Console.WriteLine("RadioButton!");
            }

            return string.Join("\n", ret);
        }
    }
}
