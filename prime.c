/* Copyright (c) 2012 the authors listed at the following URL, and/or
   the authors of referenced articles or incorporated external code:
   http://en.literateprograms.org/Miller-Rabin_primality_test_(C,_GMP)?action=history&offset=20060620215321
   
   Permission is hereby granted, free of charge, to any person obtaining
   a copy of this software and associated documentation files (the
   "Software"), to deal in the Software without restriction, including
   without limitation the rights to use, copy, modify, merge, publish,
   distribute, sublicense, and/or sell copies of the Software, and to
   permit persons to whom the Software is furnished to do so, subject to
   the following conditions:
   
   The above copyright notice and this permission notice shall be
   included in all copies or substantial portions of the Software.
   
   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
   EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
   MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
   IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
   CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
   TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
   SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
   
   Retrieved from: http://en.literateprograms.org/Miller-Rabin_primality_test_(C,_GMP)?oldid=6350
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <gmp.h>
#include <time.h>

#define COMPOSITE        0
#define PROBABLE_PRIME   1

int miller_rabin_pass(mpz_t a, mpz_t n) {
     int i, s, result;
     mpz_t a_to_power, d, n_minus_one;
     
     mpz_init(n_minus_one);
     mpz_sub_ui(n_minus_one, n, 1);
     
     s = 0;
     mpz_init_set(d, n_minus_one);
     while (mpz_even_p(d)) {
          mpz_fdiv_q_2exp(d, d, 1);
          s++;
     }
     
     mpz_init(a_to_power);
     mpz_powm(a_to_power, a, d, n);
     if (mpz_cmp_ui(a_to_power, 1) == 0) {
          result=PROBABLE_PRIME; goto exit;
     }
     for(i=0; i < s-1; i++) {
          if (mpz_cmp(a_to_power, n_minus_one) == 0) {
               result=PROBABLE_PRIME; goto exit;
          }
          mpz_powm_ui (a_to_power, a_to_power, 2, n);
     }
     if (mpz_cmp(a_to_power, n_minus_one) == 0) {
          result=PROBABLE_PRIME; goto exit;
     }
     result = COMPOSITE;
exit:
     mpz_clear(a_to_power);
     mpz_clear(d);
     mpz_clear(n_minus_one);
     return result;
}


int miller_rabin(mpz_t n, gmp_randstate_t rand_state) {
     mpz_t a;
     int repeat;
     mpz_init(a);
     for(repeat=0; repeat<20; repeat++) {
          do {
               mpz_urandomm(a, rand_state, n);
          } while (mpz_sgn(a) == 0);
          if (miller_rabin_pass(a, n) == COMPOSITE) {
               return COMPOSITE;
          }
     }
     return PROBABLE_PRIME;
}
int main(int argc, char* argv[]) {
     mpz_t n, max, two, p;
     gmp_randstate_t rand_state;
     gmp_randinit_default(rand_state);
     gmp_randseed_ui (rand_state, time(NULL));
     if (strcmp(argv[1], "test") == 0) {
          mpz_init_set_str(n, argv[2], 10);
          puts(miller_rabin(n, rand_state) == PROBABLE_PRIME ? "PRIME" : "COMPOSITE");
     } else if (strcmp(argv[1], "genprime") == 0) {
          mpz_init(max);
          mpz_init_set_ui(two, 2);
          mpz_mul_2exp(max, two, atoi(argv[2])+1);
          mpz_init(p);
          do {
               mpz_urandomm(p, rand_state, max);
               if (mpz_even_p(p)) continue;
               if (mpz_fdiv_ui(p, 3) == 0) continue;
               if (mpz_fdiv_ui(p, 5) == 0) continue;
               if (mpz_fdiv_ui(p, 7) == 0) continue;
          } while (miller_rabin(p, rand_state) == COMPOSITE);
          mpz_out_str(stdout, 10, p);
          puts("");
     }
     return 0;
}
