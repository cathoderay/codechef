{-
 Problem: Life, the Universe, and Everything
 URL: http://www.codechef.com/problems/TEST

 Author: Ronald Kaiser
 Email: raios dot catodicos at gmail dot com

 Note: This is a first approach of a Haskell solution.
 I'm still learning Haskell.
-}

is42 :: String -> Bool
is42 x = x == "42"

main = do
    input <- getLine
    if is42 input 
        then return ()
        else do 
            putStrLn input 
            main

