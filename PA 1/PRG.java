
public class PRG 
{
	public static long prgOutput[] = {210205973, 22795300, 58776750, 121262470, 264731963, 140842553, 242590528, 195244728, 86752752};
	public static long p = 295075153L;
	
	public static void main(String[] args)
	{
		long x,y;
		long startTime = System.currentTimeMillis();
		for (long i = 0; i <= p; i++)
		{
			x = i;
			y = x ^ prgOutput[0];
			long nthOutput = getNthOutput(x,y);
			if (nthOutput != -1)
			{
				System.out.println((prgOutput.length + 1) + "th output of the PRG: " + nthOutput);
				long endTime = System.currentTimeMillis();
				System.out.println("	Elapsed time: " + (endTime - startTime)  + "ms.");
				break;
			}
		}
	}

	private static long getNthOutput(long x, long y) 
	{
		for (int j = 1; j < prgOutput.length; j++)
		{
			x = (2*x + 5) % p;
			y = (3*y + 7) % p;
			if ((x ^ y) != prgOutput[j])
				return -1;
		}
		x = (2*x + 5) % p;
		y = (3*y + 7) % p;
		return (x ^ y);
	}
}
