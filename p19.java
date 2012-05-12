public class p19
{
   public  p19()
   {
      
   }
   public static int month(int m, int y)
   {
      switch(m)
      {
         case 1: return 31; 
         case 3: return 31; 
         case 4: return 30; 
         case 5: return 31; 
         case 6: return 30; 
         case 7: return 31; 
         case 8: return 31; 
         case 9: return 30; 
         case 10: return 31; 
         case 11: return 30; 
         case 12: return 31; 
         case 2: if (y % 4 == 0)
         { return 29;}
         else return 28;
         default: return -1;
            
      }
   }

   public static void solve()
   {
      int fday = 1;
      int year = 1900;
      int month = 1;

   }

   public static void main(String[] args)
   {
      for (int i = 1; i <= 12; i++)
         System.out.println(month(i,1999));
   }
}
